from django.contrib import admin
from .models import Route


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('name', 'travel_times', 'from_city', 'to_city')
    search_fields = ('name',)
