from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('homeroom.views',
    url(r'^homeroom/$', 'homeroom', name='homeroom'),
    url(r'^homeroom/class/(?P<section_id>\d+)/$', 'class_section'),
    url(r'^$', 'homeroom', name='home'),
)
