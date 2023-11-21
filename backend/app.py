from asyncio.windows_events import NULL
from operator import mod
from pyexpat import model
from flask import Flask, render_template, request,jsonify
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
from flask_cors import CORS

base = declarative_base()           #Alchemy
motor = create_engine("mysql://root:@localhost/base_sports")  #Alchemy

class User(base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key = True)
    nombre =  Column(String(50), nullable = False, unique = True)       #Base de usuarios
    contra =  Column(String(50), nullable = False, unique = False)
    def __str__(self):
        return self.nombre
    
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
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'               #Conecto Flask
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'base_sports_2'

mysql = MySQL(app)

@app.route("/inicio_sesion", methods=["POST","GET"])           #Iniciar sesion
def Inicio_sesion():
    print("entrooooo")
    consulta = sesion1.query(User).filter(
                User.nombre == request.json["nombre"]
            ).first()
    consulta1 = sesion1.query(User).filter(
                User.contra == request.json["contra"]
                ).first()

    if consulta != None and consulta1 !=None:
        response = str(consulta.nombre)
        print(type(response))
        print(response)
        msg={
            "sesion":"verdad",
            "nombre":response,
            "mensaje":"Sesion iniciada"
        }
        return msg
    else:
        msg={
            "sesion":"falso",
            "mensaje":"Datos erroneos intente de nuevo"
        }
        msg1 = jsonify(msg)
        return msg1
@app.route("/crear", methods=["POST","GET"])  #Crear un usuario
def createUser():
    consulta_ruta1 = sesion1.query(User).filter(
        User.nombre == request.json["nombre"],
        User.contra == request.json["contra"]
    ).first()
    print("datos",consulta_ruta1)
    if consulta_ruta1 == None:
        print(request.json)
        sesion1.add(User(nombre = request.json["nombre"], contra = request.json["contra"]))
        sesion1.commit()
        msg = {
            "mensaje":"cuenta creada", 
            "cuenta":"nueva"
        }
        return msg
    elif consulta_ruta1 !=None:
        msg = {
            "mensaje":"Cuenta existente",
            "cuenta":"existente"
        }
        return msg

if __name__ == '__main__':
    #base.metadata.drop_all(motor)
    #base.metadata.create_all(motor)
    app.run(debug=True)