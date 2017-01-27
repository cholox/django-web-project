"""
@Date:   2017-01-27T13:06:52+01:00
@Email:  choloisaza@outlook.de
@Last modified time: 2017-01-27T13:07:25+01:00
"""


from django.contrib import admin

from .models import Item

admin.site.register(Item)
