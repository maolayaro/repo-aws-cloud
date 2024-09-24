
import pymysql

endpoint = 'ins-bd.cl0o4cyeqk1l.us-west-1.rds.amazonaws.com'
user = 'admin'
password = 'Maor.1033734720'
database = 'db_registro'

def connectionSQL():
    connection = None
    try:
        # Establecer la conexión
        connection = pymysql.connect(  # Aquí se debe usar '='
            host=endpoint,
            user=user,
            password=password,
            database=database
        )
        print("Conexión exitosa a la base de datos")
        return connection
    except pymysql.MySQLError as err:
        print("Error al conectar a la base de datos:", err)
        return None
    finally:
        # Cerrar la conexión si está abierta
        if connection:
            connection.close()

def add_registro(Nombre, Cargo, ID, Actividad, Descripcion, Fecha, Tiempo):
    try:
        instruction_sql = "INSERT INTO registro (Nombre, Cargo, ID, Actividad, Descripcion, Fecha, Tiempo) VALUES('Maira', 'ing', 12234, 'fw', 'regla', '2024-09-24',14)"
        connection = connectionSQL()
        cursor = connection.cursor() 
        cursor.execute(instruction_sql)
        connection.commit()
        #obj_connection.commit()
        #print("Se registro la actividad con exito")
    except Exception as err:
        print("Error al conectar a la base de datos:", err)



