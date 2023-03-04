import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'product',
    'socialmedia'
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kernel.urls'


TEMPLATE_DIR = os.path.join(BASE_DIR, config('TEMPLATE_DIR'))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'kernel.wsgi.application'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

###################
# STATIC
###################


STATIC_URL = config('STATIC_URL')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, config('STATIC_DIR')),
    )

STATIC_ROOT = os.path.join(BASE_DIR, config('COLLECT_STATIC_DIR'))

MEDIA_URL = config('MEDIA_URL')

MEDIA_ROOT = config('MEDIA_UPLOAD_DIR')

FIXTURES_DIRS =config('FIXTURES_TEST_DIRS', cast=tuple)
