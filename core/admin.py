from django.contrib import admin
from core.models import Profile, Country, ProvinceState, \
    Institute, Contact, Faculty, Specialization, FacultyAssign, \
    SpecializationAssign, Badge, BadgeAssign, Course, Section, \
    SectionAssign

class ContactInline(admin.StackedInline):
    model = Contact
    extra = 0

class FacultyAssignInline(admin.TabularInline):
    model = FacultyAssign
    extra = 0

class SpecializationAssignInline(admin.TabularInline):
    model = SpecializationAssign
    extra = 0

class BadgeAssignInline(admin.TabularInline):
    model = BadgeAssign
    extra = 2

class SectionAssignInline(admin.TabularInline):
    model = SectionAssign
    
class ProfileAdmin(admin.ModelAdmin):
    inlines = [FacultyAssignInline, SpecializationAssignInline, ContactInline, BadgeAssignInline, SectionAssignInline]
    
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Country)
admin.site.register(ProvinceState)
admin.site.register(Institute)
admin.site.register(Contact)
admin.site.register(Faculty)
admin.site.register(Specialization)
admin.site.register(Badge)
admin.site.register(Course)
admin.site.register(Section)