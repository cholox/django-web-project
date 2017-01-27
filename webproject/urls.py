"""
@Date:   2017-01-26T21:45:47+01:00
@Email:  choloisaza@outlook.de
@Last modified time: 2017-01-27T12:56:42+01:00
"""

from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^', include('webproject.apps.base.urls')),
    url(r'^search/', include('webproject.apps.search.urls')),
    url(r'^item/', include('webproject.apps.item.urls')),
    url(r'^admin/', admin.site.urls),
]
