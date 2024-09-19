
import pymysql

endpoint = 'ins-bd.cl0o4cyeqk1l.us-west-1.rds.amazonaws.com'
user = 'admin'
password = 'Maor.1033734720'

def connectionSQL():
    connection = None
    try:
        # Establecer la conexión
        pymysql.connect(
            host=endpoint,
            user=user,
            password=password
        )
        print("Conexión exitosa a la base de datos")
    except pymysql.MySQLError as err:
        print("Error al conectar a la base de datos:", err)
    finally:
        # Cerrar la conexión si está abierta
        if connection:
            connection.close()

connectionSQL()
