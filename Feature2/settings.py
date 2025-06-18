import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
ALLOWED_HOSTS = []

ROOT_URLCONF = "urls"
MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
]

INSTALLED_APPS = []


