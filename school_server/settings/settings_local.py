from school_server.settings.settings import *

ENVIRONMENT = "Local"
print(f"{ENVIRONMENT} environment")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'school_db',
        'USER': 'starguard',
        'PASSWORD': 'starguard',
        'HOST': '0.0.0.0',
        'PORT': '5432',
    }
}