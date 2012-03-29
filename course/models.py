from django.db import models
from django.contrib.auth.models import User
from core.models import Institute
from core.abstract_models import SentContent
from core.constants import DURATION


class Course(models.Model):

    title = models.CharField(max_length=100)
    abbrev = models.CharField(max_length=10, verbose_name='abbreviation', null=True, blank=True)
    institute = models.ForeignKey(Institute)
    description = models.TextField(null=True, blank=True)
    difficulty = models.PositiveIntegerField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s (%s)' % (self.title, self.abbrev)

    class Meta:
        db_table = 'mva_course'
        unique_together = ('title', 'abbrev', 'institute')


class Section(models.Model):

    course = models.ForeignKey(Course)
    start_date = models.DateField()
    duration = models.CharField(max_length=1, choices=DURATION, default='T')
    user = models.ManyToManyField(User, through='SectionAssign')

    def __unicode__(self):
        return '%s [%s, %s]' % (self.course, unicode(self.start_date), self.get_duration_display())

    class Meta:
        db_table = 'mva_section'
        unique_together = ('course', 'start_date', 'duration')


class SectionAssign(models.Model):

    user = models.ForeignKey(User, related_name='%(class)s_user')
    section = models.ForeignKey(Section, related_name='%(class)s_section')

    def __unicode__(self):
        return '%s : %s' % (self.user, self.section)

    class Meta:
        db_table = 'mva_section_assign'
        verbose_name = 'section assignment'
        verbose_name_plural = 'section assignments'
        unique_together = ('user', 'section')


class Review(SentContent):

    course = models.ForeignKey(Course)

    def __unicode__(self):
        return 'To %s: %s...' % (self.course, self.message[:10])

    class Meta:
        db_table = 'mva_review'
