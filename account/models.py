from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from core.models import (Institute, ProvinceState,
    SpecializationAssign, SkillAssign)
from course.models import SectionAssign
from core.constants import (ROLE, DEGREE, GRADE,
    GRADE_MAX, GRADE_MIN, GRADE_STEP)
from core.utilities import unique_username


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
    grade = models.IntegerField(choices=GRADE, default=0)
    grade_gauge = models.IntegerField(default=0)
    influence = models.IntegerField(default=0)

    def __unicode__(self):
        return '%s' % (self.user.get_full_name())

    @staticmethod
    def register_user(email, password, first_name, last_name, institute, role):
        user = User()
        user.username = unique_username(first_name, last_name)
        user.email = email
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.is_active = False
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

    def increment_grade(self, delta):
        self.grade_gauge += delta
        if self.grade_gauge >= GRADE_STEP:
            self.grade += 1
            self.grade_gauge -= GRADE_STEP
            if self.grade >= GRADE_MAX:
                self.grade = GRADE_MAX
                self.grade_gauge = 100
        elif self.grade_gauge <= -GRADE_STEP:
            self.grade -= 1
            self.grade_gauge += GRADE_STEP
            if self.grade <= GRADE_MIN:
                self.grade = GRADE_MIN
                self.grade_gauge = -100
        self.save()

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
