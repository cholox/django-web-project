from django.shortcuts import render, redirect
from django.views import generic
from django.db.models import Q

from webproject.apps.item.models import Item


class GlobalSearchView(generic.ListView):
    template_name = 'search/search.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        """Search the items in the database"""
        query = self.request.GET.get('searchinput')
        item_list = []
        if query:
            item_list = Item.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
            # TODO: redirect to item app
        return item_list
