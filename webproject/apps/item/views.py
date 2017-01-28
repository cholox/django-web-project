from django.shortcuts import render
from django.views import generic

from .models import Item


class ItemListView(generic.ListView):
    template_name = 'item/list.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        return Item.objects.all()
