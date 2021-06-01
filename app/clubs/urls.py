from django.urls import path

from .views import ClubListView, ClubDetailView, PlayerListView, \
    PlayerDetailView, TeamListView, TeamDetailView, ClubHomeTemplateView


urlpatterns = [
    path('', ClubHomeTemplateView.as_view(), name='club_home'),
    path('clubs/', ClubListView.as_view(), name='club_list'),
    path('club/<str:slug>/', ClubDetailView.as_view(), name='club_detail'),
    path('teams/', TeamListView.as_view(), name='team_list'),
    path('team/<str:slug>/', TeamDetailView.as_view(), name='team_detail'),
    path('players/', PlayerListView.as_view(), name='player_list'),
    path('player/<str:slug>/', PlayerDetailView.as_view(), name='player_detail'),
]
