from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from .views import HomeTemplateView

urlpatterns = patterns('',
    url(r'^$', HomeTemplateView.as_view(), name='home'),
    url(r'^clubs/', include('clubs.urls')),
    url(r'^competitions/', include('competitions.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
