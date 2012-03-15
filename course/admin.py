from django.contrib import admin
from course.models import (Course, Section, SectionAssign, Review)


class ReviewInline(admin.StackedInline):
    model = Review
    extra = 0


class SectionInline(admin.TabularInline):
    model = Section
    extra = 1


class SectionAssignInline(admin.TabularInline):
    model = SectionAssign
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    inlines = [SectionInline, ReviewInline]
    list_display = ('title', 'abbrev', 'institute', 'modified_time',)
    list_filter = ('institute', 'modified_time',)
    search_fields = ['title', 'abbrev']


admin.site.register(Course, CourseAdmin)
admin.site.register(Section)
admin.site.register(Review)
