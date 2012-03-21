from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('course.views',
    url(r'^homeroom/$', 'homeroom', name='homeroom'),
    url(r'^source_course/', 'source_course'),
)
