from django.contrib import admin
from core.models import Profile, Country, ProvinceState, \
    Institute, Contact, Faculty, Specialization, FacultyAssign, \
    SpecializationAssign, Badge, BadgeAssign, Course, Section, \
    SectionAssign, Encouragement, Review, Feedback

class ContactInline(admin.StackedInline):
    model = Contact
    extra = 0

class EncouragementInline(admin.StackedInline):
    model = Encouragement
    fk_name = 'person_to'
    extra = 1

class FeedbackInline(admin.StackedInline):
    model = Feedback
    fk_name = 'instructor'
    extra = 1
    
class ReviewInline(admin.StackedInline):
    model = Review
    extra = 1
    
class FacultyAssignInline(admin.TabularInline):
    model = FacultyAssign
    extra = 0

class SpecializationAssignInline(admin.TabularInline):
    model = SpecializationAssign
    extra = 0

class BadgeAssignInline(admin.TabularInline):
    model = BadgeAssign
    extra = 2

class SectionInline(admin.TabularInline):
    model = Section
    extra = 2
    
class SectionAssignInline(admin.TabularInline):
    model = SectionAssign
    
class ProfileAdmin(admin.ModelAdmin):
    inlines = [ContactInline, FacultyAssignInline, SpecializationAssignInline, SectionAssignInline, BadgeAssignInline, EncouragementInline, FeedbackInline]

class CourseAdmin(admin.ModelAdmin):
    inlines = [SectionInline, ReviewInline]
    
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Country)
admin.site.register(ProvinceState)
admin.site.register(Institute)
admin.site.register(Contact)
admin.site.register(Faculty)
admin.site.register(Specialization)
admin.site.register(Badge)
admin.site.register(Course, CourseAdmin)
admin.site.register(Section)
admin.site.register(Encouragement)
admin.site.register(Review)
admin.site.register(Feedback)