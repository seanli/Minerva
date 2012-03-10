from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from core.constants import CATEGORY


class Country(models.Model):

    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'mva_country'
        verbose_name_plural = "countries"


class ProvinceState(models.Model):

    name = models.CharField(max_length=100)
    abbrev = models.CharField(max_length=5, verbose_name='abbreviation', null=True, blank=True)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'mva_province_state'
        verbose_name = 'province/state'
        verbose_name_plural = "provinces/states"


class Institute(models.Model):

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=1, choices=CATEGORY)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    province_state = models.ForeignKey(ProvinceState, verbose_name='province/state')
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'mva_institute'


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
    first_day = models.DateField()
    last_day = models.DateField()
    instructor = models.ForeignKey(User, related_name="%(class)s_instructor")
    user = models.ManyToManyField(User, through='SectionAssign')

    def __unicode__(self):
        return "%s [%s, %s]" % (self.course, unicode(self.first_day), unicode(self.instructor))

    class Meta:
        db_table = 'mva_section'
        unique_together = ("course", "first_day", "last_day", "instructor")


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
