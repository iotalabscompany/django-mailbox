import logging

from django.conf import settings
import requests
from social.apps.django_app.default.models import UserSocialAuth
from social_django.utils import load_strategy


logger = logging.getLogger(__name__)


class AccessTokenNotFound(Exception):
    pass


def get_google_consumer_key():
    return settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY


def get_google_consumer_secret():
    return settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET


def get_google_access_token(email):
    try:
        social = UserSocialAuth.objects.get(uid=email, provider="google-oauth2")
        return social.get_access_token(load_strategy())
    except UserSocialAuth.DoesNotExist:
        raise AccessTokenNotFound


def _oauth_headers(email):
    return dict(
        Authorization="Bearer %s" % get_google_access_token(email),
    )


def google_api_get(email, url):
    r = requests.get(url, headers=_oauth_headers(email))
    r.raise_for_status()
    try:
        return r.json()
    except ValueError:
        return r.text


def google_api_post(email, url, post_data):
    r = requests.post(url, data=post_data, header=_oauth_headers(email))
    r.raise_for_status()
    try:
        return r.json()
    except ValueError:
        return r.text


def fetch_user_info(email):
    result = google_api_get(
        email,
        "https://www.googleapis.com/oauth2/v1/userinfo?alt=json"
    )
    return result
