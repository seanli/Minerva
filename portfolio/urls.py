from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('portfolio.views',
    url(r'^portfolio/$', 'portfolio', name='portfolio'),
    url(r'^portfolio/(?P<username>\w+)/$', 'portfolio'),
)
