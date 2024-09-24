from flask import Flask, render_template, request
from database.db import *
app = Flask(__name__)

@app.route('/Tarea')
def Tarea():
    print("HOLA")
    return render_template("Tarea.html")

@app.route('/Registro', methods=['POST'])
def Registro():
    data_registro = request.form
    Nombre = data_registro["Nombre"]
    Cargo = data_registro["Cargo"]
    ID = data_registro["ID"]
    Actividad = data_registro["Actividad"]
    Descripcion = data_registro["Descripcion"]
    Fecha = data_registro["Fecha"]
    Tiempo = data_registro["Tiempo"]
    print(data_registro)
    add_registro(Nombre, Cargo, ID, Actividad, Descripcion, Fecha, Tiempo)
    return "User added"

if __name__ == "__main__":
    ip = "172.31.20.168"
    port = 80
    app.run(host=ip, port=port)  # Especificar 'host' y 'port'