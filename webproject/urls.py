"""
@Date:   2017-01-26T21:45:47+01:00
@Email:  choloisaza@outlook.de
@Last modified time: 2017-01-26T22:13:32+01:00
"""

from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^home/', include('webproject.base.urls')),
    url(r'^search/', include('webproject.search.urls')),
    url(r'^admin/', admin.site.urls),
]
