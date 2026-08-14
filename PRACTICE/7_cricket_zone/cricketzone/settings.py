from pathlib import Path

# =========================================================
# BASE DIRECTORY
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# =========================================================
# SECURITY
# =========================================================

SECRET_KEY = "django-insecure-change-this-later"

DEBUG = True

ALLOWED_HOSTS = []


# =========================================================
# INSTALLED APPS
# =========================================================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "booking",
]


# =========================================================
# MIDDLEWARE
# =========================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# =========================================================
# URL CONFIGURATION
# =========================================================

ROOT_URLCONF = "cricketzone.urls"


# =========================================================
# TEMPLATES
# =========================================================

TEMPLATES = [
    {
        "BACKEND":
            "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "templates",
        ],

        "APP_DIRS": True,

        "OPTIONS": {
            "context_processors": [

                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",

            ],
        },
    },
]


# =========================================================
# WSGI
# =========================================================

WSGI_APPLICATION = "cricketzone.wsgi.application"


# =========================================================
# DATABASE
# =========================================================

DATABASES = {
    "default": {
        "ENGINE":
            "django.db.backends.sqlite3",

        "NAME":
            BASE_DIR / "db.sqlite3",
    }
}


# =========================================================
# PASSWORD VALIDATION
# =========================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME":
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },

    {
        "NAME":
            "django.contrib.auth.password_validation.MinimumLengthValidator",
    },

    {
        "NAME":
            "django.contrib.auth.password_validation.CommonPasswordValidator",
    },

    {
        "NAME":
            "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# =========================================================
# LANGUAGE / TIMEZONE
# =========================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True


# =========================================================
# STATIC FILES
# =========================================================

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"


# =========================================================
# MEDIA FILES
# =========================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# =========================================================
# DEFAULT PRIMARY KEY
# =========================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# =========================================================
# EMAIL CONFIGURATION
# =========================================================

EMAIL_BACKEND = (
    "django.core.mail.backends.smtp.EmailBackend"
)

EMAIL_HOST = "smtp.gmail.com"

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_HOST_USER = "sahilvakahariya@gmail.com"

# IMPORTANT:
# અહીં Gmail App Password નાખવો.
# Normal Gmail password નહીં.
EMAIL_HOST_PASSWORD = "bkev nvuc wovb gxyw"

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

from dotenv import load_dotenv
load_dotenv()
# =========================================================
# 7 CRICKET ZONE OWNER EMAIL
# =========================================================

OWNER_EMAIL = "sahilvakahariya@gmail.com"


# =========================================================
# 7 CRICKET ZONE UPI PAYMENT
# =========================================================

UPI_ID = "sahilvakahariya-1@okicici"

UPI_PAYEE_NAME = "7 Cricket Zone"


# =========================================================
# OWNER WHATSAPP
# =========================================================

OWNER_WHATSAPP = "917016038813"