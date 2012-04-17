from django.contrib import admin
from course.models import (Course, Section, SectionAssign,
    Review, CourseRating, WhiteboardPost, WhiteboardComment)


class CourseRatingInline(admin.TabularInline):
    model = CourseRating
    extra = 1


class ReviewInline(admin.StackedInline):
    model = Review
    extra = 0


class SectionInline(admin.TabularInline):
    model = Section
    extra = 1


class SectionAssignInline(admin.TabularInline):
    model = SectionAssign
    extra = 1


class WhiteboardPostInline(admin.StackedInline):
    model = WhiteboardPost
    extra = 0


class WhiteboardCommentInline(admin.StackedInline):
    model = WhiteboardComment
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    inlines = [SectionInline, CourseRatingInline, ReviewInline]
    list_display = ('title', 'abbrev', 'institute', 'modified_time',)
    list_filter = ('institute', 'modified_time',)
    search_fields = ['title', 'abbrev']


class SectionAdmin(admin.ModelAdmin):
    inlines = [WhiteboardPostInline]


class WhiteboardPostAdmin(admin.ModelAdmin):
    inlines = [WhiteboardCommentInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Review)
admin.site.register(WhiteboardPost, WhiteboardPostAdmin)
