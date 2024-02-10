
Terminal commands for performing specific task
# For creating migrations 

 ## On local environment
    python manage.py makemigrations --settings=school_server.settings.settings_local
    python manage.py migrate --settings=school_server.settings.settings_local

 ## On staging environment
    python manage.py makemigrations --settings=school_server.settings.settings_stage
    python manage.py migrate --settings=school_server.settings.settings_stage

# For running server  on local env
    python manage.py runserver --settings=school_server.settings.settings_local

# For running server on stage env
    python manage.py runserver --settings=school_server.settings.settings_stage