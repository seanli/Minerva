from django.contrib import admin
from core.models import Profile, Country, ProvinceState, \
    Institute, Contact, Faculty, Specification

class ContactInline(admin.StackedInline):
    model = Contact
    extra = 0

class ProfileAdmin(admin.ModelAdmin):
    inlines = [ContactInline]
    
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Country)
admin.site.register(ProvinceState)
admin.site.register(Institute)
admin.site.register(Contact)
admin.site.register(Faculty)
admin.site.register(Specification)