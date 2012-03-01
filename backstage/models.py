from django.db import models
from django.contrib.auth.models import User
from Minerva.core.constants import (TICKET_PRIORITY, TICKET_TYPE)


class Ticket(models.Model):

    summary = models.CharField(max_length=100)
    reporter = models.ForeignKey(User, related_name="%(class)s_reporter", null=True, blank=True)
    owner = models.ForeignKey(User, related_name="%(class)s_owner", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    priority = models.PositiveIntegerField(choices=TICKET_PRIORITY, null=True, blank=True)
    type = models.CharField(max_length=1, choices=TICKET_TYPE, null=True, blank=True)
    modified_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s...' % self.summary[:10]

    class Meta:
        db_table = 'bsg_ticket'
