from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from core.models import Institute, ProvinceState
from core.constants import (DEGREE, GRADE,
    GRADE_MAX, GRADE_MIN, GRADE_STEP)
from core.utilities import generate_username


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
    def register_user(email, password, first_name, last_name, institute):
        user = User()
        user.username = generate_username()
        user.email = email
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.is_active = False
        user.save()
        profile = Profile()
        profile.user = user
        profile.institute = institute
        profile.save()

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
