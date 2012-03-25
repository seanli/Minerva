from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('backstage.views',
    url(r'^backstage/tickets/$', 'tickets', name='backstage_tickets'),
    url(r'^backstage/tickets/(?P<ticket_id>\d+)/$', 'tickets'),
    url(r'^backstage/wiki/$', 'wiki', name='backstage_wiki'),
    url(r'^backstage/wiki/(?P<wiki_id>\d+)/$', 'wiki'),
    url(r'^backstage/dashboard/$', 'dashboard', name='backstage_dashboard'),
    url(r'^backstage/$', 'dashboard', name='backstage'),
    url(r'^onerror/$', 'onerror'),
)
