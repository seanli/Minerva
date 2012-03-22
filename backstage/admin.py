from django.contrib import admin
from backstage.models import Ticket, Wiki, WikiAttachmentAssign


class TicketAdmin(admin.ModelAdmin):
    list_display = ('summary', 'priority', 'category', 'status', 'created_time', 'modified_time',)
    search_fields = ['summary', 'description']


class WikiAttachmentAssignInline(admin.TabularInline):
    model = WikiAttachmentAssign
    extra = 1


class WikiAdmin(admin.ModelAdmin):
    inlines = [WikiAttachmentAssignInline]
    list_display = ('title', 'author', 'created_time', 'modified_time')


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Wiki, WikiAdmin)
