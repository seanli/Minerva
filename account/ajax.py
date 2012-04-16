from dajaxice.decorators import dajaxice_register
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import simplejson
from django.conf import settings
from account.utilities import fake_login


@dajaxice_register
@login_required
def swap_user(request, username):
    status = 'OK'
    if not settings.SWAP_USER:
        status = 'INVALID'
    else:
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            logout(request)
            fake_login(request, user)
        except User.DoesNotExist:
            status = 'INVALID'
    return simplejson.dumps({'status': status})
