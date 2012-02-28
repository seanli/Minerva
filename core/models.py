from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from datetime import datetime
from Minerva.core.references import ROLE, DEGREE, CATEGORY
from Minerva.core.utilities import unique_username


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


@receiver(pre_save, sender=User)
def user_pre_save(sender, **kwargs):

    ''' Ensures Django User's e-mail is unique '''

    email = kwargs['instance'].email
    username = kwargs['instance'].username
    if sender.objects.filter(email=email).exclude(username=username).count() and email:
        raise ValidationError('User email needs to be unique')


class Profile(models.Model):

    ''' Extends the Django User '''

    user = models.OneToOneField(User)
    role = models.CharField(max_length=1, choices=ROLE)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    tagline = models.TextField(null=True, blank=True)
    institute = models.ForeignKey(Institute, null=True, blank=True)
    degree = models.CharField(max_length=2, choices=DEGREE, null=True, blank=True)
    influence = models.IntegerField(default=0)

    def __unicode__(self):
        return "%s" % (self.user.get_full_name())

    @staticmethod
    def register_user(email, password, first_name, last_name, institute, role):
        user = User()
        user.username = unique_username(first_name, last_name)
        user.email = email
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        profile = Profile()
        profile.user = user
        profile.institute = institute
        profile.role = role
        profile.save()

    def add_specialization(self, specialization):
        assign = SpecializationAssign()
        assign.specialization = specialization
        assign.user = self.user
        assign.save()

    def has_specialization(self, specialization):
        return SpecializationAssign.objects.filter(specialization=specialization, user=self.user).count() > 0

    def add_skill(self, skill):
        assign = SkillAssign()
        assign.skill = skill
        assign.user = self.user
        assign.save()

    def has_skill(self, skill):
        return SkillAssign.objects.filter(skill=skill, user=self.user).count() > 0

    def add_section(self, section):
        assign = SectionAssign()
        assign.section = section
        assign.user = self.user
        assign.save()

    def has_section(self, section):
        return SectionAssign.objects.filter(section=section, user=self.user).count() > 0

    class Meta:
        db_table = 'mva_profile'


# Adding functions to User class

def user_role(self):
    return self.get_profile().get_role_display()
user_role.short_description = 'Role'
User.add_to_class('user_role', user_role)


def user_institute(self):
    return '<a href="/admin/core/institute/%s/" target="_blank">%s</a>' % (self.get_profile().institute.id, self.get_profile().institute)
user_institute.allow_tags = True
user_institute.short_description = 'Institute'
User.add_to_class('user_institute', user_institute)


class Specialization(models.Model):

    name = models.CharField(max_length=100, unique=True)
    user = models.ManyToManyField(User, through='SpecializationAssign')
    modified_time = models.DateTimeField(default=datetime.now(), auto_now=True)

    def __unicode__(self):
        return self.name

    @staticmethod
    def exist(name):
        return Specialization.objects.filter(name=name).count() > 0

    @staticmethod
    def get(name):
        if Specialization.exist(name):
            return Specialization.objects.filter(name=name)[0]
        else:
            return None

    class Meta:
        db_table = 'mva_specialization'


class SpecializationAssign(models.Model):

    user = models.ForeignKey(User, related_name="%(class)s_user")
    specialization = models.ForeignKey(Specialization, related_name="%(class)s_specialization")

    def __unicode__(self):
        return "%s : %s" % (self.user, self.specialization)

    class Meta:
        db_table = 'mva_specialization_assign'
        verbose_name = 'specialization assignment'
        verbose_name_plural = 'specialization assignments'
        unique_together = ("user", "specialization")


class Skill(models.Model):

    name = models.CharField(max_length=100)
    user = models.ManyToManyField(User, through='SkillAssign')
    modified_time = models.DateTimeField(default=datetime.now(), auto_now=True)

    def __unicode__(self):
        return self.name

    @staticmethod
    def exist(name):
        return Skill.objects.filter(name=name).count() > 0

    @staticmethod
    def get(name):
        if Skill.exist(name):
            return Skill.objects.filter(name=name)[0]
        else:
            return None

    class Meta:
        db_table = 'mva_skill'


class SkillAssign(models.Model):

    user = models.ForeignKey(User, related_name="%(class)s_user")
    skill = models.ForeignKey(Skill, related_name="%(class)s_skill")

    def __unicode__(self):
        return "%s : %s" % (self.user, self.skill)

    class Meta:
        db_table = 'mva_skill_assign'
        verbose_name = 'skill assignment'
        verbose_name_plural = 'skill assignments'
        unique_together = ("user", "skill")


class Contact(models.Model):

    label = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    province_state = models.ForeignKey(ProvinceState, verbose_name='province/state')
    telephone = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name='e-mail')

    def __unicode__(self):
        return self.label

    class Meta:
        db_table = 'mva_contact'


class Badge(models.Model):

    label = models.CharField(max_length=100)
    prev_lvl = models.OneToOneField("self", null=True, blank=True, related_name="%(class)s_prev_lvl", verbose_name='previous level')
    req_exp = models.PositiveIntegerField(default=0, verbose_name='requirement EXP')
    next_exp = models.PositiveIntegerField(default=0, verbose_name='next level EXP')
    next_lvl = models.OneToOneField("self", null=True, blank=True, related_name="%(class)s_next_lvl", verbose_name='next level')
    user = models.ManyToManyField(User, through='BadgeAssign')
    # picture = models.ImageField(null=True, blank=True)

    def __unicode__(self):
        return self.label

    class Meta:
        db_table = 'mva_badge'


class BadgeAssign(models.Model):

    user = models.ForeignKey(User, related_name="%(class)s_user")
    badge = models.ForeignKey(Badge, related_name="%(class)s_badge")
    obtained = models.BooleanField(default=False)
    exp = models.PositiveIntegerField(default=0, verbose_name='EXP')

    def __unicode__(self):
        return "%s : %s" % (self.user, self.badge)

    class Meta:
        db_table = 'mva_badge_assign'
        verbose_name = 'badge assignment'
        verbose_name_plural = 'badge assignments'
        unique_together = ("user", "badge")


class Course(models.Model):

    title = models.CharField(max_length=100)
    abbrev = models.CharField(max_length=10, verbose_name='abbreviation', null=True, blank=True)
    institute = models.ForeignKey(Institute)
    description = models.TextField(null=True, blank=True)
    difficulty = models.PositiveIntegerField(null=True, blank=True)
    modified_time = models.DateTimeField(default=datetime.now(), auto_now=True)

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


class Encouragement(models.Model):

    person_to = models.ForeignKey(User, related_name="%(class)s_person_to", verbose_name='to')
    message = models.TextField()
    person_from = models.ForeignKey(User, related_name="%(class)s_person_from", verbose_name='from')
    sent_time = models.DateTimeField(default=datetime.now())
    anonymous = models.BooleanField(default=False)

    def __unicode__(self):
        return "To %s: %s..." % (self.person_to, self.message[:10])

    class Meta:
        db_table = 'mva_encouragement'


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


class Feedback(models.Model):

    instructor = models.ForeignKey(User)
    message = models.TextField()
    person_from = models.ForeignKey(User, related_name="%(class)s_person_from", verbose_name='from')
    sent_time = models.DateTimeField(default=datetime.now())
    anonymous = models.BooleanField(default=True)

    def __unicode__(self):
        return "To %s: %s..." % (self.instructor, self.message[:10])

    class Meta:
        db_table = 'mva_feedback'


class Report(models.Model):

    message = models.TextField()
    reporter = models.ForeignKey(User, related_name="%(class)s_reporter", null=True, blank=True)
    sent_time = models.DateTimeField(default=datetime.now())

    def __unicode__(self):
        return "%s: %s..." % (self.reporter, self.message[:10])

    class Meta:
        db_table = 'mva_report'
