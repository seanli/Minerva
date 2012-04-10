from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('course.views',
    url(r'^courses/$', 'courses', name='courses'),
    url(r'^courses/(?P<course_id>\d+)/$', 'courses'),
)
