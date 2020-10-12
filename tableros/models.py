from datetime import datetime

from django.db import models


class Tablero(models.Model):
    ESTADOS_TABLERO = (
        ('Iniciado', 'Iniciado'),
        ('Finalizado', 'Finalizado'),
        ('Cancelado', 'Cancelado'),
    )

    id_tablero = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=256)
    descripcion = models.CharField(max_length=256)
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
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nombre'], name='unique_nombre_tablero'),
        ]

    #     ordering = ["nombre"]
    #     permissions = (
    #                       ("asignar_equipo", "Puede asignar un usuario al proyecto"),
    #                       ("asignar_flujo", "Puede asignar un flujo al proyecto"),
    #                       ("asignar_sprint", "Puede asignar un Sprint a un Flujo-Proyecto"),
    #                       ("reasignar_sprint", "puede reasignar un Sprint a un Flujo-Proyecto"),
    #                       ("registrar_avance_userstory", "Se logea las horas trabajadas y un comentario"),
    #                       ("reportes_generales", "Se puede observar los reportes generales"),
    #                   )

    def as_json(self):
        return dict(
            id=self.id_tablero,
            nombre=self.nombre,
            descripcion=self.descripcion,
            activo=self.activo,
            fecha_modificacion=self.fecha_modificacion.isoformat()
        )


class Usuario(models.Model):
    ESTADOS_USUARIO = (
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    )

    id_usuario = models.AutoField(primary_key=True)
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    fecha_registro = models.DateField(default=datetime.now)
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    correo = models.CharField(max_length=256)
    usuario = models.CharField(max_length=256)
    contrasenha = models.CharField(max_length=256)
    estado = models.CharField(max_length=15, choices=ESTADOS_USUARIO, default='Activo')

    # QUE DATO DEVUELVE AL INVOCAR A UNA INSTANCIA DE USUARIO SIN ACCEDER A UN ATRIBUTO ESPECÍFICO
    def __unicode__(self):
        return self.usuario

    # CONFIGURACIONES EXTRA QUE PUEDEN REALIZARSE SOBRE LA CLASE USUARIO
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['usuario'], name='unique_usuario_usuario'),
        ]


class Equipo(models.Model):
    ESTADOS_EQUIPO = (
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    )

    id_equipo = models.AutoField(primary_key=True)
    id_tablero = models.IntegerField()
    id_usuario = models.IntegerField()
    nombre_equipo = models.CharField(max_length=256)
    estado = models.CharField(max_length=15, choices=ESTADOS_EQUIPO, default='Activo')

    # QUE DATO DEVUELVE AL INVOCAR A UNA INSTANCIA DE EQUIPO SIN ACCEDER A UN ATRIBUTO ESPECÍFICO
    def __unicode__(self):
        return self.nombre_equipo

    # CONFIGURACIONES EXTRA QUE PUEDEN REALIZARSE SOBRE LA CLASE EQUIPO
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nombre_equipo'], name='unique_nombre_equipo_equipo'),
        ]


class Rol_usuario_tablero(models.Model):
    ESTADOS_USUARIO = (
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    )

    id_rol_usuario = models.AutoField(primary_key=True)
    id_tablero = models.IntegerField()
    id_usuario = models.IntegerField()
    id_rol = models.IntegerField()
    estado = models.CharField(max_length=15, choices=ESTADOS_USUARIO, default='Activo')

    # QUE DATO DEVUELVE AL INVOCAR A UNA INSTANCIA DE Rol_usuario_tablero SIN ACCEDER A UN ATRIBUTO ESPECÍFICO
    def __unicode__(self):
        return self.id_rol_usuario

    # CONFIGURACIONES EXTRA QUE PUEDEN REALIZARSE SOBRE LA CLASE Rol_usuario_tablero
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id_tablero', 'id_usuario', 'id_rol', 'estado'],
                                    name='unique_idtableroidusuarioidrol_rol_usuario_tablero'),

        ]


class Rol(models.Model):
    ESTADOS_ROL = (
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    )

    id_rol = models.AutoField(primary_key=True)
    tipo_rol = models.IntegerField()
    estado = models.CharField(max_length=15, choices=ESTADOS_ROL, default='Activo')

    # QUE DATO DEVUELVE AL INVOCAR A UNA INSTANCIA DE Rol SIN ACCEDER A UN ATRIBUTO ESPECÍFICO
    def __unicode__(self):
        return self.tipo_rol

    # CONFIGURACIONES EXTRA QUE PUEDEN REALIZARSE SOBRE LA CLASE Rol
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['tipo_rol'], name='unique_tipo_rol_Rol'),

        ]


class Tarjeta_Usuario(models.Model):
    ESTADOS_TARJETA_USUARIO = (
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    )

    id_tarjeta_usuario = models.AutoField(primary_key=True)
    id_tarjeta = models.IntegerField()
    id_usuario = models.IntegerField()
    estado = models.CharField(max_length=15, choices=ESTADOS_TARJETA_USUARIO, default='Activo')

    # QUE DATO DEVUELVE AL INVOCAR A UNA INSTANCIA DE Tarjeta_Usuario SIN ACCEDER A UN ATRIBUTO ESPECÍFICO
    def __unicode__(self):
        return self.id_tarjeta_usuario

    # CONFIGURACIONES EXTRA QUE PUEDEN REALIZARSE SOBRE LA CLASE Tarjeta_Usuario
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id_tarjeta', 'id_usuario', 'estado'],
                                    name='unique_idtarjetaidusuario_tarjeta_usuario'),

        ]


class Tarjeta(models.Model):
    ESTADOS_TARJETA = (
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    )

    id_tarjeta = models.AutoField(primary_key=True)
    fecha_registro = models.DateField(default=datetime.now)
    fecha_limite = models.DateField(auto_now=False, auto_now_add=False)
    nombre_tarjeta = models.CharField(max_length=256)
    id_usuario = models.IntegerField()
    estado = models.CharField(max_length=15, choices=ESTADOS_TARJETA, default='Activo')

    # QUE DATO DEVUELVE AL INVOCAR A UNA INSTANCIA DE Tarjeta SIN ACCEDER A UN ATRIBUTO ESPECÍFICO
    def __unicode__(self):
        return self.nombre_tarjeta


"""
    # CONFIGURACIONES EXTRA QUE PUEDEN REALIZARSE SOBRE LA CLASE Tarjeta
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id_tarjeta', 'id_usuario', 'estado'], name='unique_idtarjetaidusuario_tarjeta'),

        ]
"""


class Fases(models.Model):
    ESTADOS_FASES = (
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    )

    id_fases = models.AutoField(primary_key=True)
    nombre_fases = models.CharField(max_length=256)
    fecha_registro = models.DateField(default=datetime.now)
    fecha_limite = models.DateField(auto_now=False, auto_now_add=False)
    nombre_tarjeta = models.CharField(max_length=256)
    id_usuario = models.IntegerField()
    id_tarjeta = models.IntegerField()
    estado = models.CharField(max_length=15, choices=ESTADOS_FASES, default='Activo')

    # QUE DATO DEVUELVE AL INVOCAR A UNA INSTANCIA DE FASES SIN ACCEDER A UN ATRIBUTO ESPECÍFICO
    def __unicode__(self):
        return self.nombre_fases


"""
    # CONFIGURACIONES EXTRA QUE PUEDEN REALIZARSE SOBRE LA CLASE FASES
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nombre_fases'], name='unique_nombrefases_fases'),

        ]
"""
