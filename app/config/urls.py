from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from .views import HomeTemplateView

admin.autodiscover()

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("clubs/", include("clubs.urls")),
    path("competitions/", include("competitions.urls")),
    # Uncomment the admin/doc line below to enable admin documentation:
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    # Uncomment the next line to enable the admin:
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls)), *urlpatterns]
