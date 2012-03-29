from django.db import models
from django.contrib.auth.models import User


class SentContent(models.Model):

    message = models.TextField()
    person_from = models.ForeignKey(User, related_name='%(class)s_person_from', verbose_name='from')
    sent_time = models.DateTimeField(auto_now_add=True)
    anonymous = models.BooleanField(default=False)

    class Meta:
        abstract = True
