from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from core.models import (SpecializationAssign, BadgeAssign,
    Encouragement, Feedback, SkillAssign)
from account.models import Profile, Contact
from course.models import Section, SectionAssign


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


class SpecializationAssignInline(admin.TabularInline):
    model = SpecializationAssign
    extra = 1


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
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_institute', 'last_login')
    list_filter = ()
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'profile__institute', 'last_login')
    filter_horizontal = ['groups', 'user_permissions']


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Contact)
