from datetime import datetime

from django.db import models


class Tablero(models.Model):

    ESTADOS_TABLERO=(
        ('Iniciado', 'Iniciado'),
        ('Finalizado', 'Finalizado'),
        ('Cancelado', 'Cancelado'),
    )

    idTablero = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=256)
    descripcion = models.CharField(max_length=256)
    estado = models.CharField(max_length=15, choices=ESTADOS_TABLERO, default='Iniciado')
    visibilidad = models.CharField(max_length=256)
    activo = models.BooleanField(default=True)
    fechaModificacion = models.DateField(default=datetime.now)

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

class Usuario(models.Model):

    ESTADOS_USUARIO=(
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    )

    idUsuario = models.AutoField(primary_key=True)
    fechaNacimiento= models.DateField(auto_now=False, auto_now_add=False)
    fechaRegistro = models.DateField(default=datetime.now)
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

    ESTADOS_EQUIPO=(
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    )

    idEquipo = models.AutoField(primary_key=True)
    idTablero = models.IntegerField()
    idUsuario = models.IntegerField()
    nombreEquipo = models.CharField(max_length=256)
    estado = models.CharField(max_length=15, choices=ESTADOS_EQUIPO, default='Activo')


    # QUE DATO DEVUELVE AL INVOCAR A UNA INSTANCIA DE EQUIPO SIN ACCEDER A UN ATRIBUTO ESPECÍFICO
    def __unicode__(self):
        return self.nombreEquipo

    # CONFIGURACIONES EXTRA QUE PUEDEN REALIZARSE SOBRE LA CLASE EQUIPO
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nombreEquipo'], name='unique_nombreEquipo_equipo'),
        ]

class Rol_usuario_tablero(models.Model):

    ESTADOS_USUARIO=(
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    )

    idRolUsuario = models.AutoField(primary_key=True)
    idTablero = models.IntegerField()
    idUsuario = models.IntegerField()
    idRol = models.IntegerField()
    estado = models.CharField(max_length=15, choices=ESTADOS_USUARIO, default='Activo')


    # QUE DATO DEVUELVE AL INVOCAR A UNA INSTANCIA DE Rol_usuario_tablero SIN ACCEDER A UN ATRIBUTO ESPECÍFICO
    def __unicode__(self):
        return self.idRolUsuario

    # CONFIGURACIONES EXTRA QUE PUEDEN REALIZARSE SOBRE LA CLASE Rol_usuario_tablero
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['idTablero', 'idUsuario', 'idRol', 'estado'], name='unique_idTableroidUsuarioidRol_Rol_usuario_tablero'),

        ]

class Rol(models.Model):

    ESTADOS_ROL=(
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    )

    idRol = models.AutoField(primary_key=True)
    tipoRol = models.IntegerField()
    estado = models.CharField(max_length=15, choices=ESTADOS_ROL, default='Activo')


    # QUE DATO DEVUELVE AL INVOCAR A UNA INSTANCIA DE Rol SIN ACCEDER A UN ATRIBUTO ESPECÍFICO
    def __unicode__(self):
        return self.TipoRol

    # CONFIGURACIONES EXTRA QUE PUEDEN REALIZARSE SOBRE LA CLASE Rol
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['tipoRol'], name='unique_TipoRol_Rol'),

        ]

class Tarjeta_Usuario(models.Model):

    ESTADOS_TARJETA_USUARIO=(
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    )

    idTarjetaUsuario = models.AutoField(primary_key=True)
    idTarjeta = models.IntegerField()
    idUsuario = models.IntegerField()
    estado = models.CharField(max_length=15, choices=ESTADOS_TARJETA_USUARIO, default='Activo')


    # QUE DATO DEVUELVE AL INVOCAR A UNA INSTANCIA DE Tarjeta_Usuario SIN ACCEDER A UN ATRIBUTO ESPECÍFICO
    def __unicode__(self):
        return self.idTarjetaUsuario

    # CONFIGURACIONES EXTRA QUE PUEDEN REALIZARSE SOBRE LA CLASE Tarjeta_Usuario
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['idTarjeta', 'idUsuario', 'estado'], name='unique_idTarjetaidUsuario_Tarjeta_Usuario'),

        ]

class Tarjeta(models.Model):

    ESTADOS_TARJETA=(
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    )

    idTarjeta = models.AutoField(primary_key=True)
    fechaRegistro = models.DateField(default=datetime.now)
    fechaLimite= models.DateField(auto_now=False, auto_now_add=False)
    nombreTarjeta = models.CharField(max_length=256)
    idUsuario = models.IntegerField()
    estado = models.CharField(max_length=15, choices=ESTADOS_TARJETA, default='Activo')


    # QUE DATO DEVUELVE AL INVOCAR A UNA INSTANCIA DE Tarjeta SIN ACCEDER A UN ATRIBUTO ESPECÍFICO
    def __unicode__(self):
        return self.nombreTarjeta
"""
    # CONFIGURACIONES EXTRA QUE PUEDEN REALIZARSE SOBRE LA CLASE Tarjeta
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['idTarjeta', 'idUsuario', 'estado'], name='unique_idTarjetaidUsuario_Tarjeta'),

        ]
"""

class Fases(models.Model):

    ESTADOS_FASES=(
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    )

    idFases = models.AutoField(primary_key=True)
    nombreFases = models.CharField(max_length=256)
    fechaRegistro = models.DateField(default=datetime.now)
    fechaLimite= models.DateField(auto_now=False, auto_now_add=False)
    nombreTarjeta = models.CharField(max_length=256)
    idUsuario = models.IntegerField()
    idTarjeta = models.IntegerField()
    estado = models.CharField(max_length=15, choices=ESTADOS_FASES, default='Activo')


    # QUE DATO DEVUELVE AL INVOCAR A UNA INSTANCIA DE FASES SIN ACCEDER A UN ATRIBUTO ESPECÍFICO
    def __unicode__(self):
        return self.nombreFases
"""
    # CONFIGURACIONES EXTRA QUE PUEDEN REALIZARSE SOBRE LA CLASE FASES
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nombreFases'], name='unique_nombreFases_fases'),

        ]
"""