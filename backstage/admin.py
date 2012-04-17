from django.contrib import admin
from backstage.models import (Ticket, Wiki,
    WikiAttachmentAssign, WikiRevisionHistory, LogMessage)


class TicketAdmin(admin.ModelAdmin):
    list_display = ('summary', 'priority', 'category', 'status', 'created_time', 'modified_time',)
    search_fields = ['summary', 'description']


class WikiAttachmentAssignInline(admin.TabularInline):
    model = WikiAttachmentAssign
    extra = 1


class WikiRevisionHistoryInline(admin.StackedInline):
    model = WikiRevisionHistory
    extra = 0


class WikiAdmin(admin.ModelAdmin):
    inlines = [WikiAttachmentAssignInline, WikiRevisionHistoryInline]
    list_display = ('title', 'author', 'created_time', 'modified_time')


class LogMessageAdmin(admin.ModelAdmin):
    list_display = ('logger_name', 'level', 'logged_time', 'message',)


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Wiki, WikiAdmin)
admin.site.register(LogMessage, LogMessageAdmin)
