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


@app.route('/api/usuarios', methods=['POST'])
def guardar_dato():
    conexion = conexion_db()
    print("de pana")
    data = request.get_json()  # Obtén los datos JSON de la solicitud
    cursor = conexion.cursor()

    query = "INSERT INTO usuarios (nick, rol, nombre, apellido, correo) VALUES (%s, %s, %s, %s, %s)"

    # data_id = cursor.lastrowid
    user_nick = data.get("nick")
    user_rol = data.get("rol")
    user_nombre = data.get("nombre")
    user_apellido = data.get("apellido")
    user_correo = data.get("correo")

    valores = (user_nick, user_rol, user_nombre, user_apellido, user_correo)

    consultar(query, valores)
    
    return jsonify(valores)
    # Verifica que se hayan proporcionado los campos necesarios en los datos JSON
    # if 'campo1' in data and 'campo2' in data:
    #     cursor = conexion.cursor()
    #     insert_query = "INSERT INTO datos (id, dato) VALUES (%s, %s)"
    #     values = (data['campo1'], data['campo2'])

    #     cursor.execute(insert_query, values)
    #     conexion.commit()
    #     cursor.close()

    #     return jsonify({"mensaje": "Dato guardado con éxito"})

    # return jsonify({"error": "Faltan campos en los datos JSON"}), 400


# Ruta para consultar usuarios en la base de datos
@app.route('/usuarios')
def obtener_usuarios():
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM datos")
    result = cursor.fetchall()
    cursor.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
