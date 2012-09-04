from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('account.views',
    url(r'^login/', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^signup/$', 'signup', name='signup'),
    url(r'^settings/$', 'settings', name='settings'),
    url(r'^facebook_login/', 'facebook_login', name='facebook_login'),
)
