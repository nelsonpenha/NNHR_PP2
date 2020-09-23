--Tabla Usuario
create table usuario(
	idUsuario serial primary key,
	fechaNacimineto date,
	fechaRegistro date,
	nombre varchar(256) not null unique,
	apellido varchar(256) null,
	correo varchar(256) not null unique,
	contrasenha varchar(256) not null unique,
	status varchar (100) null
	
);

--Tabla tablero
create table tablero(
	idTablero serial primary key,
	nombreTablero varchar(256) not null unique,
	visibilidad varchar(256) not null unique,
	status varchar (100) null
	
);

--Tabla equipo
create table equipo(
	idEquipo serial primary key,
	idTablero integer not null,
	idUsuario integer not null,
	nombreEquipo varchar(256) not null unique,
	status varchar (100) null
);

--Tabla rol_usuario_tablero
create table rol_usuario_tablero(
	idRol_U serial primary key,
	idTablero integer not null,
	idUsuario integer not null,
	idRol integer not null
);

--Tabla rol
create table rol(
	idRol serial primary key,
	tipoRol varchar(100) not null unique,
	status varchar (100) null
);

--Tabla tarjeta_Usuario
create table tarjeta_por_usuario(
	idTarjeta_Usuario serial primary key,
	idTarjeta integer not null,
	idUsuario integer not null
);
--Tabla tarjeta
create table tarjeta(
	idTarjeta serial primary key,
	fechaLimite date,
	fechaRegistro date,
	nombreTarjeta varchar(256) not null unique,
	status varchar (100) null,
	idUsuario integer not null
);
--Tabla fases
create table fases(
	idFases serial primary key,
	fechaLimite date,
	fechaRegistro date,
	nombreTarjeta varchar(256) not null unique,
	status varchar (100) null,
	idTarjeta integer not null,
	idTablero integer not null
);