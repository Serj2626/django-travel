from django.contrib import admin
from trains.models import Train, TrainTest


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ['name', 'travel_time', 'from_city', 'to_city']
    list_editable = ['travel_time']
    search_fields = ['name']


# @admin.register(TrainTest)
# class TrainTestAdmin(admin.ModelAdmin):
#     list_display = ['name', 'from_city']
