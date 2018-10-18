# django-masterpass

## Installation

###Install with pip:

    pip install django-masterpass
    
##Usage:

add in `AUTHENTICATION_BACKEND` setting value `django_masterpass.auth.MasterPass`:

        AUTHENTICATION_BACKEND = [..., 'django_masterpass.auth.MasterPass']            
    
add in settings value MASTER_PASS:
    
    MASTER_PASS='password'