from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('crowd.views',
    url(r'^crowd/$', 'crowd', name='crowd'),
    url(r'^crowd/(?P<username>\w+)/$', 'crowd'),
)
