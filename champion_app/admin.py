from django.contrib import admin
from .models import Champion
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ChampionResources(resources.ModelResource):

    class Meta:
        model = Champion

class ChampionAdmin(ImportExportModelAdmin):
    resources_champion = ChampionResources



admin.site.register(ChampionResources, ChampionAdmin)