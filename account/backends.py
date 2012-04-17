from django.contrib.auth.models import User


class EmailAuthBackend(object):

    ''' Custom authentication backend to allow username/email login '''

    def authenticate(self, username=None, password=None):
        if '@' in username:
            try:
                user = User.objects.get(email__iexact=username)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                return None
        else:
            try:
                user = User.objects.get(username__iexact=username)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    supports_object_permissions = True
    supports_anonymous_user = True
    supports_inactive_user = True
