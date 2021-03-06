from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ads.views.home', name='home'),
    url(r'^search', 'ads.views.search', name='search'),
    url(r'^get_progress', 'ads.views.search_progress', name='search_progress'),
    # url(r'^kijiji_rentals/', include('kijiji_rentals.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
