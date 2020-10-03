from datetime import datetime

from django.db import models


class Tablero(models.Model):

    ESTADOS_TABLERO=(
        ('Iniciado', 'Iniciado'),
        ('Finalizado', 'Finalizado'),
        ('Cancelado', 'Cancelado'),
    )

    id_tablero = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    estado = models.CharField(max_length=15, choices=ESTADOS_TABLERO, default='Iniciado')
    visibilidad = models.CharField(max_length=256)
    activo = models.BooleanField(default=True)
    fecha_modificacion = models.DateField(default=datetime.now)

    # EJEMPLO DE LÓGICA AL GUARDAR/MODIFICAR UN TABLERO
    # def save(self):
    #     from datetime import timedelta
    #     d = timedelta(days=self.duracion_estimada*7)
    #     if self.fecha_inicio:
    #      self.fecha_final = self.fecha_inicio + d
    #      super(Proyecto, self).save()
    #     else:
    #      self.fecha_final = self.fecha_final
    #      super(Proyecto, self).save()

    # QUE DATO DEVUELVE AL INVOCAR A UNA INSTANCIA DE TABLERO SIN ACCEDER A UN ATRIBUTO ESPECÍFICO
    def __unicode__(self):
        return self.nombre

    # CONFIGURACIONES EXTRA QUE PUEDEN REALIZARSE SOBRE LA CLASE TABLERO
    # class Meta:
    #     ordering = ["nombre"]
    #     permissions = (
    #                       ("asignar_equipo", "Puede asignar un usuario al proyecto"),
    #                       ("asignar_flujo", "Puede asignar un flujo al proyecto"),
    #                       ("asignar_sprint", "Puede asignar un Sprint a un Flujo-Proyecto"),
    #                       ("reasignar_sprint", "puede reasignar un Sprint a un Flujo-Proyecto"),
    #                       ("registrar_avance_userstory", "Se logea las horas trabajadas y un comentario"),
    #                       ("reportes_generales", "Se puede observar los reportes generales"),
    #                   )