# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def principal():
#     return "Bienvenidos primera prueba"
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'usuario'
mysql = MySQL(app)


@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacto')
    data = cur.fetchall()
    return render_template('/index.html', contactos=data)


@app.route('/add_contact')
def add_contact():
    return 'Add_contact'


@app.route('/edit')
def edit():
    return 'edit'


@app.route('/delete')
def delete():
    return 'delete'


if __name__ == '__main__':
    app.run(port=300, debug=True)
