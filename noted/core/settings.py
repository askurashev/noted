"""
Django settings for NoteD project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

from dotenv import load_dotenv

from django.utils.translation import gettext_lazy as _


# Parse a `.env` file and load the variables inside into environment variables
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = BASE_DIR.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG_SET")

SITE_ID = 1

ALLOWED_HOSTS = ["welel-noted.site", "www.welel-noted.site"]
ALLOWED_HOSTS.append(os.getenv("IP"))
if DEBUG:
    ALLOWED_HOSTS += ["127.0.0.1", "localhost"]

CSRF_TRUSTED_ORIGINS = ["https://welel-noted.site", "http://welel-noted.site"]

ADMINS = [(os.getenv("ADMIN_NAME"), os.getenv("ADMIN_EMAIL"))]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.github",
    "allauth.socialaccount.providers.yandex",
    "taggit",
    "simplemde",
    "rosetta",
    "common.apps.CommonConfig",
    "users.apps.UsersConfig",
    "content.apps.ContentConfig",
    "tags.apps.TagsConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "common.middleware.WwwRedirectMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

if not DEBUG:
    SECURE_SSL_REDIRECT = True

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            PROJECT_DIR.joinpath("frontend/templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# The project uses PostgreSQL database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DATABASE_NAME"),
        "USER": os.getenv("DATABASE_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": os.getenv("DATABASE_HOST"),
        "PORT": os.getenv("DATABASE_PORT"),
    }
}

AUTH_USER_MODEL = "users.User"

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

FILE_HANDLER = {
    "class": "logging.handlers.RotatingFileHandler",
    "maxBytes": 1048576,
    "backupCount": 10,
    "formatter": "verbose",
}
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "\n\n{levelname}\n{asctime}\n{name} {module} on line: {lineno}\n{message}",
            "style": "{",
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "include_html": True,
        },
        "file_django": dict(
            FILE_HANDLER,
            filename=PROJECT_DIR.joinpath("logs/django.log"),
            level="WARNING",
        ),
        "file_request": dict(
            FILE_HANDLER,
            filename=PROJECT_DIR.joinpath("logs/request.log"),
            level="DEBUG",
        ),
        "file_sql": dict(
            FILE_HANDLER,
            filename=PROJECT_DIR.joinpath("logs/sql.log"),
            level="WARNING",
        ),
        "file_exceptions": dict(
            FILE_HANDLER,
            filename=PROJECT_DIR.joinpath("logs/exceptions.log"),
            level="WARNING",
        ),
        "file_views_exceptions": dict(
            FILE_HANDLER,
            filename=PROJECT_DIR.joinpath("logs/views_exceptions.log"),
            level="WARNING",
        ),
        "file_emails": dict(
            FILE_HANDLER,
            filename=PROJECT_DIR.joinpath("logs/emails.log"),
            level="INFO",
        ),
        "file_markdown": dict(
            FILE_HANDLER,
            filename=PROJECT_DIR.joinpath("logs/markdown.log"),
            level="WARNING",
        ),
        "file_content_views": dict(
            FILE_HANDLER,
            filename=PROJECT_DIR.joinpath("logs/content_views.log"),
            level="INFO",
        ),
        "file_users_views": dict(
            FILE_HANDLER,
            filename=PROJECT_DIR.joinpath("logs/users_views.log"),
            level="INFO",
        ),
    },
    "loggers": {
        "django": {"handlers": ["file_django"], "level": "WARNING"},
        "django.request": {
            "handlers": ["file_request"],
            "level": "DEBUG",
        },
        "django.db.backends": {
            "handlers": ["file_sql"],
            "level": "WARNING",
        },
        "exceptions": {
            "handlers": ["file_exceptions"],
            "level": "WARNING",
        },
        "views.exceptions": {
            "handlers": ["file_views_exceptions"],
            "level": "WARNING",
        },
        "emails": {
            "handlers": ["file_emails"],
            "level": "INFO",
        },
        "markdown": {
            "handlers": ["file_markdown"],
            "level": "WARNING",
        },
        "content.views.note": {
            "handlers": ["file_content_views"],
            "level": "INFO",
        },
        "users.views": {
            "handlers": ["file_users_views"],
            "level": "INFO",
        },
    },
}

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = "en"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
LOCALE_PATHS = (PROJECT_DIR.joinpath("frontend/locale/"),)
LANGUAGES = (
    ("en", _("English")),
    ("ru", _("Russian")),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_ROOT = PROJECT_DIR.joinpath("frontend/collected_static")
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    PROJECT_DIR.joinpath("frontend/static"),
]

MEDIA_URL = "/media/"
MEDIA_ROOT = PROJECT_DIR.joinpath("frontend/media")
DEFAULT_USER_AVATAR_PATH = "user/default_avatar.jpg"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Simple Mail Transfer Protocol (SMTP) configuration.
# The project uses Yandex SMTP.
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST = "smtp.yandex.ru"
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
SERVER_EMAIL = os.getenv("EMAIL_HOST_USER")
DEFAULT_FROM_EMAIL = os.getenv("EMAIL_HOST_USER")
EMAIL_PORT = 465

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SOCIALACCOUNT_ADAPTER = "users.adapter.SocialAccountAdapter"
ACCOUNT_DEFAULT_HTTP_PROTOCOL = os.getenv("HTTP_PROTOCOL")
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
SOCIALACCOUNT_LOGIN_ON_GET = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 10
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_USERNAME_MIN_LENGTH = 3
SOCIALACCOUNT_EMAIL_VERIFICATION = False
SOCIALACCOUNT_PROVIDERS = {
    "yandex": {
        "APP": {
            "client_id": os.getenv("YANDEX_ID"),
            "secret": os.getenv("YANDEX_SECRET"),
            "SCOPE": ["email"],
        }
    },
    "github": {
        "APP": {
            "client_id": os.getenv("GITHUB_ID"),
            "secret": os.getenv("GITHUB_SECRET"),
            "SCOPE": ["email"],
        }
    },
    "google": {
        # CLIENT_ID and SECRET provieds via admin site.
        "SCOPE": [
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        "OAUTH_PKCE_ENABLED": True,
    },
}

TAGGIT_CASE_INSENSITIVE = True
TAGGIT_TAGS_FROM_STRING = "tags.utils.custom_tag_string"
