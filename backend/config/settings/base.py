"""Base settings for the project.

For more information on this file, see:
    https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see:
    https://docs.djangoproject.com/en/dev/ref/settings/

"""
import environ

# (/backend/config/settings/base.py - 3 = /backend)
# or inside docker container is path /app
APPS_DIR = environ.Path(__file__) - 3

# load operating system environment variables and then prepare to use them
env = environ.Env()

# DEBUG
DEBUG = env.bool('DJANGO_DEBUG', default=False)


# APPLICATIONS
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.admin',
]
THIRD_PARTY_APPS = [
    'health_check',
    'health_check.db',
    'health_check.contrib.psutil',

    'corsheaders',
]
LOCAL_APPS = ['apps.collections']
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# MIDDLEWARES
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# DATABASES
DB_USER = env('POSTGRES_USER', default='')
DB_PASSWORD = env('POSTGRES_PASSWORD', default='')
DB_PORT = env('POSTGRES_PORT', default='')
DB_NAME = env('POSTGRES_DB', default='')
DB_HOST = env('POSTGRES_HOST', default='')
DB_CONFIG_URL = 'postgres://{0}:{1}@{2}:{3}/{4}'.format(
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_NAME,
)
DATABASES = {'default': env.db('DATABASE_URL', default=DB_CONFIG_URL)}
DATABASES['default']['ATOMIC_REQUESTS'] = True


# GLOBALIZATION - I18N, L10N
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True


# TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(APPS_DIR.path('shared/templates')),
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# HTTP
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=[])


# STATIC
STATIC_ROOT = str(APPS_DIR.path('shared/static_files'))
STATIC_URL = '/static/'
STATICFILES_DIRS = [str(APPS_DIR.path('shared/static'))]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


# MEDIA
MEDIA_ROOT = str(APPS_DIR.path('shared/media'))
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'


# URLs
ROOT_URLCONF = 'config.urls'
# Location of root django.contrib.admin URL, use {% url 'admin:index' %}
ADMIN_URL = 'admin/'


# WSGI
WSGI_APPLICATION = 'config.wsgi.application'


# AUTHENTICATION
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]
# AUTH_USER_MODEL = 'users.User'  # noqa: E800
LOGIN_REDIRECT_URL = 'users:redirect'
LOGIN_URL = 'account_login'
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation'
            + '.UserAttributeSimilarityValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.MinimumLengthValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.CommonPasswordValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.NumericPasswordValidator'
        ),
    },
]


# DJANGO TEST MIGRATIONS
# NOTE: some of `django-test-migrations` settings are provided here,
# so there can be only 1 place to edit them
DTM_IGNORED_MIGRATIONS = frozenset((
    ('authtoken', '0002_auto_20160226_1747'),
))


# STAR WARS API
STAR_WARS_API_URL = env('STAR_WARS_API_URL')
