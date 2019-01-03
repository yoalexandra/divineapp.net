import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

#import socket to read host name
import socket
# If the host name starts with 'li', set LIVEHOST = True
if socket.gethostname().startswith('li'):
    LIVEHOST = True
else:
    LIVEHOST = False
# Define general behavior variables for live host and non-live host
if LIVEHOST:
    DEBUG = False
else:
    DEBUG = True

SECRET_KEY = '+&@e5l%x4$58^vb#^_xox4okl!hs8r*#h(ot(vl$s)^p-13#_d'

ALLOWED_HOSTS = ['127.0.0.1']
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'divineapp.home',
    'divineapp.blog',
    'divineapp.apps',
    'divineapp.sendemail',
    'django.forms',

]
FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'divineapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['%s/templates/'% (PROJECT_DIR),],
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

WSGI_APPLICATION = 'divineapp.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
INTERNAL_IPS = ('127.0.0.1')

STATICFILES_DIRS = ('%s/website-static-default/'% (BASE_DIR),)

ADMINS = (('webmaster', 'webmaster@divineapp.net'), ('admin', 'admin@divineapp.net'))

#TODO: - configure it
RAVEN_CONFIG = {
    'dsn': 'https://<place_your_project_dsn_here>:<place_your_project_dsn_here>@sentry.io/151850',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    #'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
}

if LIVEHOST:
    # Output to file based SMTP server on live host
    #EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST='smtp.gmail.com'
    EMAIL_PORT=587
    EMAIL_HOST_USER='alexandra.beznosova@gmail.com/OR/support@divineapp.net'
    EMAIL_HOST_PASSWORD='password'
    EMAIL_USE_TLS=True

else:
    # Output to console for non live host
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
