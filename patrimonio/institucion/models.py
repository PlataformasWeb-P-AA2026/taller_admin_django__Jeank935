from django.db import models

class Museo(models.Model):
    nombre = models.CharField(max_length=30, unique =True)
    ciudad = models.CharField(max_length=30)
    año_fundacion = models.IntegerField()


    def __str__(self):
        return f"Nombre {self.nombre} - Ciudad: {self.ciudad}- Año fundacion: {self.año_fundacion}"

class Guia_Museo(models.Model):
    nombre_completo = models.CharField(max_length=60)
    años_experiencia_guia = models.IntegerField()
    idiomas_hablados = models.CharField(max_length=100)
    museo = models.ForeignKey(Museo, on_delete=models.CASCADE)

    def __str__(self):
        return f"Nombre Completo: {self.nombre_completo}- Anios Experiencia: {self.años_experiencia_guia}- Idiomas: {self.idiomas_hablados}"

# Exhibición:
# Atributos:
# titulo_exhibicion: Título de la exhibición (cadena de texto).
# duracion_meses: Duración de la exhibición en meses (número entero).
# costo_produccion: Costo total de producción de la exhibición (número decimal).
# tematica: Temática principal de la exhibición (cadena de texto).
# Relación: una exhibición es asistida por un guía de museo
class Exhibicion(models.Model):
    titulo_exhibicion = models.CharField(max_length=100)
    duracion_meses = models.IntegerField()
    costo_produccion = models.DecimalField(max_digits=10, decimal_places=2)
    tematica = models.CharField(max_length=100)
    guia = models.ForeignKey(Guia_Museo, on_delete=models.CASCADE, \
                             related_name="guia_exhibicion")

    def __str__(self):
        return f"Titulo Exhibicion: {self.titulo_exhibicion}- Duracion Exhibicion: {self.duracion_meses}- Costo: {self.costo_produccion}- Tematica: {self.tematica}"

    