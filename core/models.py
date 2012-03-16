from django.db import models
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
