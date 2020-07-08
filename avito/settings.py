import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'pd0dy7expu@o*9ko&cfwvb76@p8y2lrt)@gm0278tfw+9h!rt-'

DEBUG = True

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'account.User'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # base apps
    'apps.account',
    'apps.main_page',
    'apps.product',

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

ROOT_URLCONF = 'avito.urls'

AVITO_TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates/')

BASE_TEMPLATES_DIRS = (
    AVITO_TEMPLATES_DIR,
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': BASE_TEMPLATES_DIRS,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]
        }
    },
]


WSGI_APPLICATION = 'avito.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'avito/../db.sqlite3'),
    }
}

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True
USE_L10N = True
USE_TZ = True

SESSION_SAVE_EVERY_REQUEST = True
SITE = 1

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


# REST API SETTINGS
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser'
    ],
    'DATETIME_FORMAT': '%Y-%m-%dT%H:%M:%SZ',
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}

CORS_ORIGIN_ALLOW_ALL = True
