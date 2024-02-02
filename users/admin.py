from django.contrib import admin
from django.contrib.admin import ModelAdmin, register

from series.models import Serie, Episode


# Register your models here.


class SeriesAdmin(ModelAdmin):
    pass

admin.site.register(Serie, SeriesAdmin)
@register(Episode)
class EpisodeAdmin(ModelAdmin):
    pass
