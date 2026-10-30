from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-change-me")
DEBUG = os.getenv("DEBUG", "True") == "True"
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

     "apps.accounts",   #авторизация
     "apps.catalog",    #каталог книг
     "apps.clients",    #читатели (покупатели)
     "apps.orders",     #заказы
     "apps.reports",    #отчеты

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'confing.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processore.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'confing.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME", "fes"),
        'USER': os.getenv("DB_USER", "fes"),
        'PASSWORD': os.getenv("DB_PASSWORD", "fes"),
        'HOST': os.getenv("DB_HOST", "localhost"),
        'PORT': os.getenv("DB_PORT", "5432"),
    }
}

AUTH_USER_MODEL = "accounts.User"

AUTH_PASSWORD_VALIDATOR = [
    {"NAME":"django.contrib.auth.password_validator.UserAttributeSimilarityValidator"},
    {"NAME":"django.contrib.auth.password_validator."},
    {"NAME":"django.contrib.auth.password_validator."},
    {"NAME":"django.contrib.auth.password_validator."},
]

CACHES = {
    'default': {
        'BACKEND': "django.core.cache.backends.redis.RedisCache",
        'LOCATION': os.getenv('REDIS_URL'),
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
