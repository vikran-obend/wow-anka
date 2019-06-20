from django.contrib import admin

from .models import Upcoming,News

# Register your models here.

admin.site.register(Upcoming)
admin.site.register(News)