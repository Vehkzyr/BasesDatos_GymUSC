# Importamos la libreria para la gestion de la base de datos
import sqlite3

# Nos conectamos a la base de datos del gimnasio de la USC
miConexion = sqlite3.connect("GimnasioUSC")

# Con la conexión, crea un objeto cursor
miCursor = miConexion.cursor()

# Creo las tablas
miCursor.execute('''
        CREATE TABLE USUARIOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT not null,
        DNI VARCHAR(9) UNIQUE not null,
        correoUSC VARCHAR(50) UNIQUE,
        NOMBRE VARCHAR (50),
        reservasTotales INTEGER,
        reservasActivas INTEGER,
        CUOTA BIT)
''')

miCursor.execute('''
        CREATE TABLE ACTIVIDADES(
        ID INTEGER PRIMARY KEY AUTOINCREMENT not null,
        NOMBRE VARCHAR (50),
        HORARIO VARCHAR(50),
        DURACION INTEGER)
''')

miCursor.execute('''
        CREATE TABLE INSTALACIONES(
        ID INTEGER PRIMARY KEY AUTOINCREMENT not null,
        NOMBRE VARCHAR (50),
        HORARIO VARCHAR(50),
        numeroPlazasMax INTEGER)
''')

miCursor.execute('''
        CREATE TABLE CUOTAS(
        ID_USUARIO INTEGER,
        ACTIVIDAD INTEGER,
        FECHA DATE,
        FOREIGN KEY(ID_USUARIO) REFERENCES USUARIOS(ID),
        FOREIGN KEY(ACTIVIDAD) REFERENCES ACTIVIDADES(ID))
''')

miCursor.execute('''
        CREATE TABLE RESERVAS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT not null,
        ID_USUARIO INTEGER,
        ACTIVIDAD INTEGER,
        HORARIO DATETIME,
        FOREIGN KEY(ID_USUARIO) REFERENCES USUARIOS(ID),
        FOREIGN KEY(ACTIVIDAD) REFERENCES ACTIVIDADES(ID))
''')

#Creamos las tablas las cuales tendrn el concepto de herencia en sql
miCursor.execute('''
    CREATE TABLE Personal (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    DNI VARCHAR(9) UNIQUE,
    correoUSC VARCHAR(50) UNIQUE,
    NOMBRE VARCHAR(50),
    HORARIO DATETIME,
    SALARIO INTEGER,
    dia_contratacion DATE,
    tiempo_trabajado INTEGER GENERATED ALWAYS AS (JULIANDAY('now') - JULIANDAY(dia_contratacion)) VIRTUAL
    );
''')

miCursor.execute('''
    CREATE TABLE Limpieza AS
    SELECT * FROM Personal
    WHERE 1 = 2
''')

miCursor.execute('''
   CREATE TABLE Monitores AS
   SELECT *, CAST(NULL AS VARCHAR(50)) AS ACTIVIDAD FROM Personal
   WHERE 1 = 2
''')

miCursor.execute('''
    CREATE TABLE Administracion AS
    SELECT *, CAST(NULL AS VARCHAR(50)) AS puestoTrabajo FROM Personal
    WHERE 1 = 2
''')


#Cierro la conexion con la base de datos
miConexion.close()
