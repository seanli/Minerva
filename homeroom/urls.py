from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('homeroom.views',
    url(r'^homeroom/$', 'homeroom', name='homeroom'),
)
