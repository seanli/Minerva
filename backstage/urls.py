from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('Minerva.backstage.views',
    url(r'^backstage/', 'home', name='backstage'),
)
