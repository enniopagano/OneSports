from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

def conexion_db():
    try:
        conexion = mysql.connector.connect(
            user = "root",
            password = "root",
            host = "192.168.44.118",
            port = "3306",
            database = "onesports"
        )
        return conexion
    except mysql.connector.Error as e:
        print(f"Error: No se puede acceder a la base de datos.\n{e}")
        return None

# Define las consultas a la base de datos
def consultar(query, values = None):
    conexion = conexion_db()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(query, values)
            conexion.commit()
    except mysql.connector.Error as e:
            print(f"Error al ejecutar la consulta:\n{e}")
    finally:
        conexion.close()

@app.route(/'login', methods = ['GET', 'POST'])
def login():
    data = request.get_json()

    user_nick = data.get("nick")
    user_contrasena = data.get("contra")

    consulta_nombre = "SELECT EXISTS(SELECT 1 FROM usuarios WHERE nick = %s)"
    consultar_nick = consultar(consulta_nombre, (user_nick,))

    consulta_contrasena = "SELECT EXISTS(SELECT 1 FROM usuarios WHERE contrasena = %s)"
    consultar_contra = consultar(consulta_contrasena, (user_contrasena,))

    if consultar_nick[0] and consultar_contra[0] != None:
        msg = {
            "sesion" : "true"
            "nombre" : user_nick
            "mensaje" : "sesion iniciada"
        }

@app.route('/crear', methods=['POST', 'GET'])
def guardar_dato():
    conexion = conexion_db()
    print("de pana")
    data = request.get_json()  # Obtén los datos JSON de la solicitud
    cursor = conexion.cursor()

    consulta_post = "INSERT INTO usuarios (nick, contrasena, correo) VALUES (%s, %s, %s)"

    user_nick = data.get("nick")
    user_contrasena = data.get("contra")
    user_correo = data.get("correo")

    valores = (user_nick, user_contrasena, user_correo)

    consulta_comprobante = "SELECT EXISTS(SELECT 1 FROM usuarios WHERE nick = %s)"

    consultar(consulta_comprobante, (user_nick,))
    comprobante = cursor.fetchone()

    if comprobante[0]:
        print("El nombre de usuario " + user_nick + " ya existe")
        msg = {
            "nombre" : "existe"
        }
        return msg
    else:
        consultar(query, valores)
        print("Usuario creado")
        msg = {
            "nombre" : user_nick
        }
        return msg 

    # return jsonify(valores)


# Ruta para consultar usuarios en la base de datos
@app.route('/usuarios')
def obtener_usuarios():
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios")
    result = cursor.fetchall()
    cursor.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
