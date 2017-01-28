"""
@Date:   2017-01-26T22:10:01+01:00
@Email:  choloisaza@outlook.de
@Last modified time: 2017-01-28T09:26:33+01:00
"""


from django.conf.urls import url

from . import views

app_name = 'search'
urlpatterns = [
    url(r'^$', views.GlobalSearchView.as_view(), name='search'),
]
