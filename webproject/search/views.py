# from django.shortcuts import render
from django.http import HttpResponse


def global_search(request):
    return HttpResponse("Hello, world. SEARCH.")
