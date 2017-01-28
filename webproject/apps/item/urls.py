"""
@Date:   2017-01-27T12:55:49+01:00
@Email:  choloisaza@outlook.de
@Last modified time: 2017-01-28T11:20:20+01:00
"""


from django.conf.urls import url

from . import views

app_name = 'item'
urlpatterns = [
    url(r'^$', views.ItemListView.as_view(), name='detail'),
]
