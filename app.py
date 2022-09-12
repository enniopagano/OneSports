from distutils.util import execute
import email
from multiprocessing import connection
from unicodedata import name
from flask import Flask, jsonify, request,render_template
from flask_mysqldb import MySQL
from config import configuracion





app = Flask(__name__)

conexion = MySQL(app)
@app.route("/",methods=["GET","POST"])
def rend ():
    if request.method == "POST":
        contra = request.form["password"]  
        user = request.form["name"]
        cur = conexion.connection
        insertar = "INSERT INTO prueba (nombre,Contra) VALUES ({contra},{user})".format
        cur

    return render_template("index.html")
 
if __name__ == "__main__":
    app.config.from_object(configuracion)
    app.run(debug=True,port=5000)
