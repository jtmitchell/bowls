from django.conf.urls import patterns, url

from .views import ClubListView, ClubDetailView, PlayerListView, \
    PlayerDetailView, TeamListView, TeamDetailView, ClubHomeTemplateView


urlpatterns = patterns('',
    url(r'^$', ClubHomeTemplateView.as_view(), name='club_home'),
    url(r'^clubs/$', ClubListView.as_view(), name='club_list'),
    url(r'^club/(?P<slug>\w+)/$', ClubDetailView.as_view(), name='club_detail'),
    url(r'^teams/$', TeamListView.as_view(), name='team_list'),
    url(r'^team/(?P<slug>\w+)/$', TeamDetailView.as_view(), name='team_detail'),
    url(r'^players/$', PlayerListView.as_view(), name='player_list'),
    url(r'^player/(?P<slug>\w+)/$', PlayerDetailView.as_view(), name='player_detail'),
)
