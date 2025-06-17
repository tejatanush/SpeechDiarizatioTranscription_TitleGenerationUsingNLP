import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = "dummy-secret-key"
DEBUG = True
ALLOWED_HOSTS = []

ROOT_URLCONF = "urls"
MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
]

INSTALLED_APPS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
