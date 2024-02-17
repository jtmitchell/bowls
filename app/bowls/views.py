from django.views.generic.base import TemplateView
from utils.view_class import ResourceContextMixin


class HomeTemplateView(ResourceContextMixin, TemplateView):
    template_name = "bowls/home.html"
    resource_context = {"meta": {"title": "Welcome", "description": ""}}
