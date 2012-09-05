from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from dajaxice.core import dajaxice_autodiscover


admin.autodiscover()
dajaxice_autodiscover()

handler403 = 'core.views.error_403'
handler404 = 'core.views.error_404'
handler500 = 'core.views.error_500'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'views.home', name='home'),
    # url(r'^Minerva/', include('foo.urls')),
    # Import URLs
    url(r'', include('bulletin.urls')),
    url(r'', include('account.urls')),
    url(r'', include('homeroom.urls')),
    url(r'', include('course.urls')),
    url(r'', include('portfolio.urls')),
    url(r'', include('backstage.urls')),
    url(r'', include('data.urls')),
    # Admin URLs
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # AJAX URLs
    url(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls'))
)

# Static File URLs
urlpatterns += staticfiles_urlpatterns()
