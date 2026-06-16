from django.contrib import admin
from institucion.models import Museo, Guia_Museo, Exhibicion

class ExhibicionAdmin(admin.ModelAdmin):
    list_display = ('titulo_exhibicion', 'duracion_meses', 'costo_produccion', 'tematica')
    search_fields = ("titulo_exhibicion", 'tematica')

admin.site.register(Exhibicion, ExhibicionAdmin)


class GuiaAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'años_experiencia_guia', 'idiomas_hablados')
    search_fields = ('nombre_completo', 'años_experiencia_guia')

admin.site.register(Guia_Museo, GuiaAdmin)

class MuseoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'año_fundacion', 'get_costo_total_produccion', 'get_guia_mas_experiencia')

admin.site.register(Museo, MuseoAdmin)

