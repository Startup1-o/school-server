from school_server.settings.settings import *

ENVIRONMENT = "Staging"
print(f"{ENVIRONMENT} environment")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': {
    }
}