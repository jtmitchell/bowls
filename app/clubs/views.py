from django.views.generic import DetailView, ListView, TemplateView
from utils.view_class import ResourceContextMixin

from .models import Club, Player, Team


class ClubHomeTemplateView(ResourceContextMixin, TemplateView):
    template_name = "clubs/club_home.html"
    resource_context = {"meta": {"title": "Clubs and Players"}}


class ClubListView(ResourceContextMixin, ListView):
    model = Club
    template_name = "clubs/club_list.html"
    resource_context = {"meta": {"title": "Clubs List"}}


class ClubDetailView(ResourceContextMixin, DetailView):
    model = Club
    template_name = "clubs/club_detail.html"
    resource_context = {"meta": {"title": "Club Detail"}}


class TeamListView(ResourceContextMixin, ListView):
    model = Team
    template_name = "clubs/team_list.html"
    resource_context = {"meta": {"title": "Teams List"}}


class TeamDetailView(ResourceContextMixin, DetailView):
    model = Team
    template_name = "clubs/team_detail.html"
    resource_context = {"meta": {"title": "Team Detail"}}


class PlayerListView(ResourceContextMixin, ListView):
    model = Player
    template_name = "clubs/player_list.html"
    resource_context = {"meta": {"title": "Players List"}}


class PlayerDetailView(ResourceContextMixin, DetailView):
    model = Player
    template_name = "clubs/player_detail.html"
    resource_context = {"meta": {"title": "Player Detail"}}
