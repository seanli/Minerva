from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('bulletin.views',
    # Home Page
    url(r'^bulletin/', 'bulletin', name='bulletin'),
    url(r'^$', 'bulletin', name='home'),
)
