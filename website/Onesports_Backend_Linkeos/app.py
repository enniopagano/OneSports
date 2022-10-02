from asyncio.windows_events import NULL
from operator import mod
from pyexpat import model
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from email.policy import default
from enum import unique
import flask
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *

base = declarative_base()           #Alchemy
motor = create_engine("mysql://root:@localhost/base_sports")  #Alchemy

class User(base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key = True)
    nombre =  Column(String(50), nullable = False, unique = True)       #Base de usuarios
    contra =  Column(String(50), nullable = False, unique = False)
    def __str__(self):
        return self.Username
    
class comentario(base):
    __tablename__ = "comentarios"
    id = Column(Integer(), primary_key = True)
    comentario =  Column(String(250), nullable = False, unique = False)
    Usuario =  Column(String(50), nullable = False, unique = True)       #Base de comentarios
    
    def __str__(self):
        return self.Username


sesion = sessionmaker(motor)                #Alchemy
sesion1 = sesion()              #Alchemy
app = Flask(__name__)       #Inicializamos Flask

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'               #Conecto Flask
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'base_sports'

mysql = MySQL(app)


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/F1")
def F1():
    return render_template("F1.html")
@app.route("/Futbol")
def Futbol():
    return render_template("Futbol.html")
@app.route("/NBA")
def NBA():
    return render_template("NBA.html")
@app.route("/UFC")
def UFC():
    return render_template("UFC.html")


@app.route('/login', methods=['GET', 'POST'])  #Iniciar Sesion
def login():
    if request.method == "POST":
        print("Esto es un POST")
        try:
            print("posta1")
            nombre = request.form['nombreI']
            contra = request.form['contraI']
            print("posta2")
            
            consulta = sesion1.query(User).filter(
                User.contra == contra
            ).first()
            consulta2 = sesion1.query(User).filter(
                User.nombre == nombre
            ).first()
            print("posta3")
            if consulta != None and consulta2 !=None:
                global nombre_Usuario
                nombre_Usuario =  {
                    "nombre":consulta.nombre
                } 
                return render_template("Sesion_iniciada.html", data=nombre_Usuario)
            else:
                return render_template("No_encontrada.html")
        except Exception as ex:
            return "FALLO"
    return render_template('login.html')




@app.route('/newacc', methods=['GET', 'POST'])           #Crear cuenta
def newacc():
    if request.method == "POST":
        usuario = request.form['nombre_crear']
        contraseña = request.form['contra_crear']
        modelo = User(nombre = usuario, contra = contraseña)
        chequear = sesion1.query(User).filter(
            User.nombre == usuario 
        ).first()
        if chequear == None:
            cons = sesion1.add(modelo)
            sesion1.commit()
            print(cons)
            return render_template("Creada.html")
        else:
            return render_template("Existe.html")
    return render_template('newacc.html')


@app.route("/noticia", methods=['GET', 'POST']) #noticia
def noticia():
    print("posta1")
    if request.method == "POST":
        print("posta2")
        texto = request.form["Area_Texto"]
        Usuario_cometador = request.form["Usuario_comentando"]
        print("posta3")
        modelo = comentario(comentario = texto, Usuario = Usuario_cometador)
        print("posta4")
        insertar = sesion1.add(modelo)
        print("posta5")
        sesion1.commit()            
        comentario_total ={
            "comentario":modelo.comentario
            }
        print(modelo.comentario)
        return render_template('Noticia.html', data = comentario_total)
    return render_template('Noticia.html')


if __name__ == '__main__':
    # base.metadata.drop_all(motor)
    # base.metadata.create_all(motor)
    app.run(debug=True)

    