from django.shortcuts import render
from django.http import HttpResponse

from webproject import constants


def home(request):
    context = {"project_name": constants.PROJECT_NAME}
    return render(request, 'base/home.html', context)
