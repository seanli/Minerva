from django.conf import settings
from django.contrib.auth import load_backend, login


def fake_login(request, user):
    '''
    Log in a user without requiring credentials
    '''
    if not hasattr(user, 'backend'):
        for backend in settings.AUTHENTICATION_BACKENDS:
            if user == load_backend(backend).get_user(user.pk):
                user.backend = backend
                break
    if hasattr(user, 'backend'):
        return login(request, user)
