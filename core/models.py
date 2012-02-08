from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from datetime import datetime
from core.references import ROLE, DEGREE, CATEGORY

class Country(models.Model):
    
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'mva_country'
        verbose_name_plural = "countries"
    
class ProvinceState(models.Model):
    
    name = models.CharField(max_length=100)
    abbrev = models.CharField(max_length=5, verbose_name='abbreviation')
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
    degree = models.CharField(max_length=2, choices=DEGREE, default='UG')
    influence = models.IntegerField(default=0)
    
    def __unicode__(self):
        return "%s %s (%s)" % (self.user.first_name, self.user.last_name, self.user.username)
    
    class Meta:
        db_table = 'mva_profile'

def create_user_profile(sender, instance, created, **kwargs):
    
    ''' Handler for connecting Profile to Django User '''
    
    if created:
        Profile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)

class Faculty(models.Model):
    
    name = models.CharField(max_length=100)
    profile = models.ManyToManyField(Profile, through='FacultyAssign')
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'mva_faculty'
        verbose_name_plural = "faculties"
        
class FacultyAssign(models.Model):
    
    profile = models.ForeignKey(Profile, related_name="%(class)s_profile")
    faculty = models.ForeignKey(Faculty, related_name="%(class)s_faculty")
    
    def __unicode__(self):
        return "%s : %s" % (self.profile, self.faculty)
    
    class Meta:
        db_table = 'mva_faculty_assign'
        verbose_name = 'faculty assignment'
        verbose_name_plural = 'faculty assignments'
        unique_together = ("profile", "faculty")

class Specialization(models.Model):
    
    name = models.CharField(max_length=100)
    profile = models.ManyToManyField(Profile, through='SpecializationAssign')
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'mva_specialization'

class SpecializationAssign(models.Model):
    
    profile = models.ForeignKey(Profile, related_name="%(class)s_profile")
    specialization = models.ForeignKey(Specialization, related_name="%(class)s_specialization")
    
    def __unicode__(self):
        return "%s : %s" % (self.profile, self.specialization)
    
    class Meta:
        db_table = 'mva_specialization_assign'
        verbose_name = 'specialization assignment'
        verbose_name_plural = 'specialization assignments'
        unique_together = ("profile", "specialization")
        
class Contact(models.Model):
    
    label = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile)
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
    profile = models.ManyToManyField(Profile, through='BadgeAssign')
    # picture = models.ImageField(null=True, blank=True)
    
    def __unicode__(self):
        return self.label
    
    class Meta:
        db_table = 'mva_badge'

class BadgeAssign(models.Model):
    
    profile = models.ForeignKey(Profile, related_name="%(class)s_profile")
    badge = models.ForeignKey(Badge, related_name="%(class)s_badge")
    obtained = models.BooleanField(default=False)
    exp = models.PositiveIntegerField(default=0, verbose_name='EXP')
    
    def __unicode__(self):
        return "%s : %s" % (self.profile, self.badge)
    
    class Meta:
        db_table = 'mva_badge_assign'
        verbose_name = 'badge assignment'
        verbose_name_plural = 'badge assignments'
        unique_together = ("profile", "badge")

class Course(models.Model):
    
    name = models.CharField(max_length=100)
    abbrev = models.CharField(max_length=10, verbose_name='abbreviation')
    institute = models.ForeignKey(Institute)
    description = models.TextField(null=True, blank=True)
    difficulty = models.PositiveIntegerField(null=True, blank=True)
    
    def __unicode__(self):
        return "%s (%s)" % (self.name, self.abbrev)
    
    class Meta:
        db_table = 'mva_course'
        unique_together = ("name", "abbrev", "institute")
    
class Section(models.Model):
    
    course = models.ForeignKey(Course)
    first_day = models.DateField()
    last_day = models.DateField()
    instructor = models.ForeignKey(Profile, related_name="%(class)s_instructor")
    profile = models.ManyToManyField(Profile, through='SectionAssign')
    
    def __unicode__(self):
        return "%s [%s, %s]" % (self.course, unicode(self.first_day), unicode(self.instructor))
    
    class Meta:
        db_table = 'mva_section'

class SectionAssign(models.Model):
    
    profile = models.ForeignKey(Profile, related_name="%(class)s_profile")
    section = models.ForeignKey(Section, related_name="%(class)s_section")
    
    def __unicode__(self):
        return "%s : %s" % (self.profile, self.section)
    
    class Meta:
        db_table = 'mva_section_assign'
        verbose_name = 'section assignment'
        verbose_name_plural = 'section assignments'
        unique_together = ("profile", "section")

class Encouragement(models.Model):
    
    person_to = models.ForeignKey(Profile, related_name="%(class)s_person_to", verbose_name='to')
    message = models.TextField()
    person_from = models.ForeignKey(Profile, related_name="%(class)s_person_from", verbose_name='from')
    sent_time = models.DateTimeField(default=datetime.now())
    anonymous = models.BooleanField(default=False)
    
    def __unicode__(self):
        return "To %s: %s..." % (self.person_to, self.message[:10])
    
    class Meta:
        db_table = 'mva_encouragement'
        
class Review(models.Model):
    
    course = models.ForeignKey(Course)
    message = models.TextField()
    person_from = models.ForeignKey(Profile, related_name="%(class)s_person_from", verbose_name='from')
    sent_time = models.DateTimeField(default=datetime.now())
    anonymous = models.BooleanField(default=False)
    
    def __unicode__(self):
        return "To %s: %s..." % (self.course, self.message[:10])
    
    class Meta:
        db_table = 'mva_review'
        
class Feedback(models.Model):
    
    instructor = models.ForeignKey(Profile)
    message = models.TextField()
    person_from = models.ForeignKey(Profile, related_name="%(class)s_person_from", verbose_name='from')
    sent_time = models.DateTimeField(default=datetime.now())
    anonymous = models.BooleanField(default=True)
    
    def __unicode__(self):
        return "To %s: %s..." % (self.instructor, self.message[:10])
    
    class Meta:
        db_table = 'mva_feedback'