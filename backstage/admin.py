from django.contrib import admin
from backstage.models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ('summary', 'priority', 'category', 'status', 'created_time', 'modified_time',)
    search_fields = ['summary', 'description']

admin.site.register(Ticket, TicketAdmin)
