from django.db import models
from django.contrib.auth.models import User
from core.abstract_models import SentContent
from core.constants import INSTITUTE_CATEGORY


class Country(models.Model):

    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'mva_country'
        verbose_name_plural = 'countries'


class ProvinceState(models.Model):

    name = models.CharField(max_length=100)
    abbrev = models.CharField(max_length=5, verbose_name='abbreviation', null=True, blank=True)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'mva_province_state'
        verbose_name = 'province/state'
        verbose_name_plural = 'provinces/states'


class Institute(models.Model):

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=1, choices=INSTITUTE_CATEGORY)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    province_state = models.ForeignKey(ProvinceState, verbose_name='province/state')
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'mva_institute'


class Specialization(models.Model):

    name = models.CharField(max_length=100, unique=True)
    user = models.ManyToManyField(User, through='SpecializationAssign')
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'mva_specialization'


class SpecializationAssign(models.Model):

    user = models.ForeignKey(User, related_name='%(class)s_user')
    specialization = models.ForeignKey(Specialization, related_name='%(class)s_specialization')

    def __unicode__(self):
        return '%s : %s' % (self.user, self.specialization)

    class Meta:
        db_table = 'mva_specialization_assign'
        verbose_name = 'specialization assignment'
        verbose_name_plural = 'specialization assignments'
        unique_together = ('user', 'specialization')


class Skill(models.Model):

    name = models.CharField(max_length=100)
    user = models.ManyToManyField(User, through='SkillAssign')
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'mva_skill'


class SkillAssign(models.Model):

    user = models.ForeignKey(User, related_name='%(class)s_user')
    skill = models.ForeignKey(Skill, related_name='%(class)s_skill')

    def __unicode__(self):
        return '%s : %s' % (self.user, self.skill)

    class Meta:
        db_table = 'mva_skill_assign'
        verbose_name = 'skill assignment'
        verbose_name_plural = 'skill assignments'
        unique_together = ('user', 'skill')


class Badge(models.Model):

    label = models.CharField(max_length=100)
    prev_lvl = models.OneToOneField('self', null=True, blank=True, related_name='%(class)s_prev_lvl', verbose_name='previous level')
    req_exp = models.PositiveIntegerField(default=0, verbose_name='requirement EXP')
    next_exp = models.PositiveIntegerField(default=0, verbose_name='next level EXP')
    next_lvl = models.OneToOneField('self', null=True, blank=True, related_name='%(class)s_next_lvl', verbose_name='next level')
    user = models.ManyToManyField(User, through='BadgeAssign')
    # picture = models.ImageField(null=True, blank=True)

    def __unicode__(self):
        return self.label

    class Meta:
        db_table = 'mva_badge'


class BadgeAssign(models.Model):

    user = models.ForeignKey(User, related_name='%(class)s_user')
    badge = models.ForeignKey(Badge, related_name='%(class)s_badge')
    obtained = models.BooleanField(default=False)
    exp = models.PositiveIntegerField(default=0, verbose_name='EXP')

    def __unicode__(self):
        return '%s : %s' % (self.user, self.badge)

    class Meta:
        db_table = 'mva_badge_assign'
        verbose_name = 'badge assignment'
        verbose_name_plural = 'badge assignments'
        unique_together = ('user', 'badge')


class Encouragement(SentContent):

    person_to = models.ForeignKey(User, related_name='%(class)s_person_to', verbose_name='to')
    approved = models.BooleanField(default=False)

    def __unicode__(self):
        return 'To %s: %s...' % (self.person_to, self.message[:10])
    
    def approve(self, approve=True):
        self.approved = approve
        self.save()

    class Meta:
        db_table = 'mva_encouragement'


class Feedback(SentContent):

    instructor = models.ForeignKey(User)

    def __unicode__(self):
        return 'To %s: %s...' % (self.instructor, self.message[:10])

    class Meta:
        db_table = 'mva_feedback'


class WebFile(models.Model):

    name = models.CharField(max_length=100)
    item = models.FileField(upload_to='webfiles')
    uploader = models.ForeignKey(User, null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'mva_webfile'
        verbose_name = 'web file'
        verbose_name_plural = 'web files'
