"""
@Date:   2017-01-26T22:10:01+01:00
@Email:  choloisaza@outlook.de
@Last modified time: 2017-01-26T22:10:25+01:00
"""


from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
