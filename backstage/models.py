from django.db import models
from django.contrib.auth.models import User
from core.models import WebFile
from core.constants import (TICKET_PRIORITY, TICKET_CATEGORY,
    TICKET_STATUS, LOG_LEVEL)
from datetime import datetime


class Ticket(models.Model):

    summary = models.CharField(max_length=100)
    reporter = models.ForeignKey(User, related_name='%(class)s_reporter', null=True, blank=True)
    owner = models.ForeignKey(User, related_name='%(class)s_owner', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=TICKET_STATUS, default='L')
    priority = models.PositiveIntegerField(choices=TICKET_PRIORITY, null=True, blank=True)
    category = models.CharField(max_length=1, choices=TICKET_CATEGORY, null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s...' % self.summary[:10]

    class Meta:
        db_table = 'bsg_ticket'


class Wiki(models.Model):

    title = models.CharField(max_length=100)
    document = models.TextField()
    attachment = models.ManyToManyField(WebFile, through='WikiAttachmentAssign')
    author = models.ForeignKey(User, null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def save(self, user=None, *args, **kwargs):
        try:
            old_version = Wiki.objects.get(id=self.id)
        except Wiki.DoesNotExist:
            old_version = None
        super(Wiki, self).save(*args, **kwargs)
        if old_version is not None and (self.document != old_version.document or self.title != old_version.title):
            revision_history = WikiRevisionHistory()
            revision_history.wiki = self
            revision_history.title_from = old_version.title
            revision_history.title_to = self.title
            revision_history.document_from = old_version.document
            revision_history.document_to = self.document
            revision_history.modified_by = user
            revision_history.save()

    class Meta:
        db_table = 'bsg_wiki'
        verbose_name_plural = 'wiki'


class WikiRevisionHistory(models.Model):

    wiki = models.ForeignKey(Wiki)
    title_from = models.CharField(max_length=100)
    title_to = models.CharField(max_length=100)
    document_from = models.TextField()
    document_to = models.TextField()
    modified_by = models.ForeignKey(User, null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s: %s' % (self.wiki, unicode(self.created_time))

    class Meta:
        db_table = 'bsg_wiki_revision_history'
        verbose_name = 'wiki revision history'
        verbose_name_plural = 'wiki revision histories'


class WikiAttachmentAssign(models.Model):

    wiki = models.ForeignKey(Wiki)
    attachment = models.ForeignKey(WebFile)
    uploader = models.ForeignKey(User)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s : %s' % (self.wiki, self.attachment)

    class Meta:
        db_table = 'bsg_wiki_attachment_assign'
        verbose_name = 'wiki attachment assignment'
        verbose_name_plural = 'wiki attachment assignments'
        unique_together = ('wiki', 'attachment')


class LogMessage(models.Model):

    logger_name = models.CharField(max_length=100, blank=True, null=True)
    logged_time = models.DateTimeField(default=datetime.now())
    level = models.IntegerField(choices=LOG_LEVEL, blank=True, null=True)
    file_path = models.CharField(max_length=255, blank=True, null=True)
    function_name = models.CharField(max_length=255, blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    traceback = models.TextField(blank=True, null=True)
    uri_path = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)
    request = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return '%s[%s] - %s' % (self.logger_name, self.get_level_display(), unicode(self.logged_time))

    class Meta:
        db_table = 'bsg_log_message'
        verbose_name = 'log message'
        verbose_name_plural = 'log messages'
        ordering = ['-logged_time']
