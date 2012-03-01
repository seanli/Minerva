from django.contrib import admin
from Minerva.backstage.models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ('summary', 'created_time', 'modified_time',)
    search_fields = ['summary', 'description']

admin.site.register(Ticket, TicketAdmin)
