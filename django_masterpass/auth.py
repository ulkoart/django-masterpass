"""
main module
"""

import warnings

from django.contrib.auth.hashers import check_password, make_password
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

USER_MODEL = get_user_model()


class MasterPass(ModelBackend):
    """
    MasterPass authentication backend
    """
    def __init__(self):
        try:
            self.master_pass = getattr(settings, 'MASTER_PASS')
        except AttributeError:
            warnings.warn('you use django_masterpass, but not set MASTER_PASS value in settings')
            self.master_pass = None
        super(MasterPass, self).__init__()

    def __getattribute__(self, name):
        if name == 'authenticate' and not self.master_pass:
            return None
        return super(MasterPass, self).__getattribute__(name)

    def authenticate(self, request, username=None, password=None, **kwargs):
        if not self.master_pass:
            return None
        if username is None:
            username = kwargs.get(USER_MODEL.USERNAME_FIELD)
        try:
            user = USER_MODEL._default_manager.get_by_natural_key(username)
        except USER_MODEL.DoesNotExist:
            return None
        if check_password(password, make_password(self.master_pass)):
            return user
        return None
