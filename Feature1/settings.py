import os
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv("HF_KEY")
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'urls'

FILE_UPLOAD_MAX_MEMORY_SIZE = 100 * 1024 * 1024