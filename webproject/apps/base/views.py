from django.shortcuts import render
from django.views import generic

from webproject import constants


class HomeView(generic.ListView):
    template_name = 'base/home.html'
    context_object_name = 'project_name'

    def get_queryset(self):
        return constants.PROJECT_NAME
