from asyncio.windows_events import NULL
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'form'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        firstName = request.form['nombre']
        lastName = request.form['contra']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO usuario(nombre, contra) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')
@app.route('/iniciar', methods=['GET', 'POST'])
def inicio():
    if request.method == "POST":
        print("Esto es un POST")
        try:
            print("posta1")
            firstName = request.form['nombreI']
            lastName = request.form['contraI']
            cur = mysql.connection.cursor()
            print("posta2")
            cur.execute("""SELECT contra, nombre FROM usuario WHERE nombre = '{}'  and contra = '{}'""".format(firstName,lastName)) 
            print("posta3")
            mysql.connection.commit()
            lista = cur.fetchall() 
            print("tama;o",len(lista))
            if len(lista)==1:
                return render_template('sesion_exito.html')
            else:
                return render_template('fracaso.html')
        except Exception as ex:
            return "FALLO"
    return render_template('iniciar.html')
    


if __name__ == '__main__':
    app.run()