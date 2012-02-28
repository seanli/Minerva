from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from Minerva.core.models import (Profile, Country, ProvinceState,
    Institute, Contact, Specialization, SpecializationAssign,
    Badge, BadgeAssign, Course, Section,
    SectionAssign, Encouragement, Review, Feedback,
    Skill, SkillAssign, Report)


class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 0


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


class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline, ContactInline, SpecializationAssignInline, SkillAssignInline, BadgeAssignInline, SectionAssignInline, EncouragementInline, FeedbackInline]
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_role', 'user_institute', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'profile__role', 'profile__institute', 'last_login')


class CourseAdmin(admin.ModelAdmin):
    inlines = [SectionInline, ReviewInline]
    list_display = ('title', 'abbrev', 'institute', 'modified_time',)
    list_filter = ('institute', 'modified_time',)
    search_fields = ['title', 'abbrev']


class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name', 'modified_time',)
    list_filter = ('modified_time',)
    search_fields = ['name']


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'modified_time',)
    list_filter = ('modified_time',)
    search_fields = ['name']


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
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
admin.site.register(Skill, SkillAdmin)
admin.site.register(Report)
