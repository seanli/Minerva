from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('account.views',
    url(r'^login/', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^signup/$', 'signup', name='signup'),
    url(r'^crowd/$', 'crowd', name='crowd'),
    url(r'^crowd/(?P<username>\w+)/$', 'crowd'),
    url(r'^source_specialization/', 'source_specialization'),
    url(r'^source_skill/', 'source_skill'),
)
