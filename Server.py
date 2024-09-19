from flask import Flask, render_template
app = Flask (__name__)

@app.route('/Tarea')
def Tarea():
    print("HOLA")
    return render_template("Tarea.html")


if __name__ == "__main__":
    ip = "172.31.20.168"
    port = "80"
    app.run(ip, port)

rm -rf .git