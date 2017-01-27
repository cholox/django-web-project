from django.shortcuts import render


def global_search(request):
    return render(request, 'search/search.html')
