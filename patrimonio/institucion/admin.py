from django.contrib import admin
# Al momento de presentar la información de museos, se debe presentar, 
# además, el costo total de producción en función de los costos de las
#  exhibiciones y el nombre (es) del guía con más experiencia
from institucion.models import Museo,Guia_Museo,Exhibicion
class ExhibicionAdmin(admin.ModelAdmin):
    list_display = ('titulo_exhibicion', 'duracion_meses', 'costo_produccion','tematica')
    
    search_fields= ("titulo_exhibicion", 'tematica')

    def get_estudiante(self, obj):
        """ """
        return obj.estudiante.apellido
admin.site.register(Exhibicion,ExhibicionAdmin)

class MuseoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'año_fundacion', 'get_exhibicion')
    search_fields = ('nombre', 'ciudad')

    def get_exhibicion(self, obj):
        """ """
        return obj.exhibicion.costo_produccion

admin.site.register(Museo, MuseoAdmin)

