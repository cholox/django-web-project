"""
@Date:   2017-01-26T21:45:47+01:00
@Email:  choloisaza@outlook.de
@Last modified time: 2017-01-27T10:19:19+01:00
"""

from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^', include('webproject.base.urls')),
    url(r'^search/', include('webproject.search.urls')),
    url(r'^admin/', admin.site.urls),
]
