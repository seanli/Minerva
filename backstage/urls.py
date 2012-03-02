from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('Minerva.backstage.views',
    url(r'^backstage/tickets/', 'tickets', name='backstage_tickets'),
    url(r'^backstage/dashboard/', 'dashboard', name='backstage_dashboard'),
    url(r'^backstage/', 'dashboard', name='backstage'),
)
