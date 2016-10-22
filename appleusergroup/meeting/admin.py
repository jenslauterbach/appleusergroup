from django.contrib import admin

from .models import Meeting
from .models import Location

admin.site.register(Meeting)
admin.site.register(Location)
