"""
@Date:   2017-01-26T22:10:01+01:00
@Email:  choloisaza@outlook.de
@Last modified time: 2017-01-28T11:16:27+01:00
"""


from django.conf.urls import url

from . import views

app_name = 'base'
urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
]
