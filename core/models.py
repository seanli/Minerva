from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

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
    CATEGORY = (
        ('E', 'Elementary School'),
        ('M', 'Middle School'),
        ('H', 'High School'),
        ('C', 'College'),
        ('U', 'University'),
    )
    category = models.CharField(max_length=1, choices=CATEGORY)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    province_state = models.ForeignKey(ProvinceState, verbose_name='province/state')
    description = models.TextField(null=True, blank=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'mva_institute'

class Faculty(models.Model):
    
    name = models.CharField(max_length=100)
    institute = models.ForeignKey(Institute)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'mva_faculty'
        verbose_name_plural = "faculties"
        
class Specification(models.Model):
    
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'mva_specification'
        
# Extends the Django User
class Profile(models.Model):
    
    user = models.OneToOneField(User)
    ROLE = (
        ('S', 'Student'),
        ('P', 'Professor'),
        ('T', 'Tutor'),
    )
    role = models.CharField(max_length=1, choices=ROLE)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    tagline = models.TextField(null=True, blank=True)
    instutute = models.ForeignKey(Institute)
    faculty = models.ForeignKey(Faculty, null=True, blank=True)
    specification = models.ForeignKey(Specification, null=True, blank=True)
    
    def __unicode__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)
    
    class Meta:
        db_table = 'mva_profile'

# Handler for connecting Profile to Django User
def create_user_profile(sender, instance, created, **kwargs):
    
    if created:
        Profile.objects.create(user=instance)
        
post_save.connect(create_user_profile, sender=User)

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
    