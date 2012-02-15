from django.contrib import admin
from Minerva.core.models import Profile, Country, ProvinceState, \
    Institute, Contact, Specialization, SpecializationAssign, \
    Badge, BadgeAssign, Course, Section, \
    SectionAssign, Encouragement, Review, Feedback, \
    Skill, SkillAssign, Report

class ContactInline(admin.StackedInline):
    model = Contact
    extra = 0

class EncouragementInline(admin.StackedInline):
    model = Encouragement
    fk_name = 'person_to'
    extra = 0

class FeedbackInline(admin.StackedInline):
    model = Feedback
    fk_name = 'instructor'
    extra = 0
    
class ReviewInline(admin.StackedInline):
    model = Review
    extra = 0

class SpecializationAssignInline(admin.TabularInline):
    model = SpecializationAssign
    extra = 0

class SkillAssignInline(admin.TabularInline):
    model = SkillAssign
    extra = 1

class BadgeAssignInline(admin.TabularInline):
    model = BadgeAssign
    extra = 1

class SectionInline(admin.TabularInline):
    model = Section
    extra = 1
    
class SectionAssignInline(admin.TabularInline):
    model = SectionAssign
    extra = 1
    
class ProfileAdmin(admin.ModelAdmin):
    inlines = [ContactInline, SpecializationAssignInline, SkillAssignInline, SectionAssignInline, BadgeAssignInline, EncouragementInline, FeedbackInline]
    list_display = ('__unicode__', 'user_link', 'institute',)
    list_filter = ('institute',)
    search_fields = ['user__first_name', 'user__last_name', 'user__username']

class CourseAdmin(admin.ModelAdmin):
    inlines = [SectionInline, ReviewInline]
    list_display = ('title', 'abbrev', 'institute',)
    list_filter = ('institute',)
    search_fields = ['title', 'abbrev']

class SpecializationAdmin(admin.ModelAdmin):
    search_fields = ['name']
    
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Country)
admin.site.register(ProvinceState)
admin.site.register(Institute)
admin.site.register(Contact)
admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Badge)
admin.site.register(Course, CourseAdmin)
admin.site.register(Section)
admin.site.register(Encouragement)
admin.site.register(Review)
admin.site.register(Feedback)
admin.site.register(Skill)
admin.site.register(Report)