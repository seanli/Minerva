from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from core.models import Institute
from core.constants import DURATION


class Course(models.Model):

    title = models.CharField(max_length=100)
    abbrev = models.CharField(max_length=10, verbose_name='abbreviation', null=True, blank=True)
    institute = models.ForeignKey(Institute)
    description = models.TextField(null=True, blank=True)
    difficulty = models.PositiveIntegerField(null=True, blank=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s (%s)" % (self.title, self.abbrev)

    @staticmethod
    def exist(title, institute):
        return Course.objects.filter(title=title, institute=institute).count() > 0

    @staticmethod
    def get(title, institute):
        if Course.exist(title, institute):
            return Course.objects.filter(title=title, institute=institute)[0]
        else:
            return None

    class Meta:
        db_table = 'mva_course'
        unique_together = ("title", "abbrev", "institute")


class Section(models.Model):

    course = models.ForeignKey(Course)
    start_date = models.DateField()
    duration = models.CharField(max_length=1, choices=DURATION, default='T')
    user = models.ManyToManyField(User, through='SectionAssign')

    def __unicode__(self):
        return "%s [%s, %s]" % (self.course, unicode(self.start_date), unicode(self.instructor))

    class Meta:
        db_table = 'mva_section'
        unique_together = ("course", "start_date", "duration")


class SectionAssign(models.Model):

    user = models.ForeignKey(User, related_name="%(class)s_user")
    section = models.ForeignKey(Section, related_name="%(class)s_section")

    def __unicode__(self):
        return "%s : %s" % (self.user, self.section)

    class Meta:
        db_table = 'mva_section_assign'
        verbose_name = 'section assignment'
        verbose_name_plural = 'section assignments'
        unique_together = ("user", "section")


class Review(models.Model):

    course = models.ForeignKey(Course)
    message = models.TextField()
    person_from = models.ForeignKey(User, related_name="%(class)s_person_from", verbose_name='from')
    sent_time = models.DateTimeField(default=datetime.now())
    anonymous = models.BooleanField(default=False)

    def __unicode__(self):
        return "To %s: %s..." % (self.course, self.message[:10])

    class Meta:
        db_table = 'mva_review'
