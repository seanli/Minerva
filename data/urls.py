from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('data.views',
    url(r'^autocomplete_course/', 'autocomplete_course'),
    url(r'^autocomplete_specialization/', 'autocomplete_specialization'),
    url(r'^autocomplete_skill/', 'autocomplete_skill'),
)
