"""
@Date:   2017-01-27T12:55:49+01:00
@Email:  choloisaza@outlook.de
@Last modified time: 2017-01-27T13:13:31+01:00
"""


from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.item_list, name='item'),
]
