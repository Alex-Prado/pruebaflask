
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


app = Flask(__name__)

# CONEXION A LA BD
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'usuario'
mysql = MySQL(app)

# CREAR UN KEY
app.secret_key = 'myscretkey'


@app.route('/')
def Index():
    consulta = mysql.connection.cursor()
    consulta.execute('SELECT * FROM contacto')
    data = consulta.fetchall()
    return render_template('/index.html', contactos=data)


@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        lastname = request.form['lastname']
        dni = request.form['dni']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacto (nombre, apellido, telefono) VALUES (%s, %s, %s)',
                    (fullname, lastname, dni))
        mysql.connection.commit()
        flash('CONTACTO AGREGADO')
        return redirect(url_for('Index'))


@app.route('/delete/<string:id>')
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacto WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('CONTACTO ELIMINADO')
    return redirect(url_for('Index'))


@app.route('/edit/<id>')
def edit(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacto WHERE id = {0}'.format(id))
    data = cur.fetchall()
    return render_template('edit.html', contactos=data[0])


@app.route('/update/<id>', methods=['POST'])
def update(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        lastname = request.form['lastname']
        dni = request.form['dni']

        cur = mysql.connection.cursor()
        cur.execute("UPDATE contacto SET nombre = %s, apellido = %s, telefono = %s  WHERE id = %s", (fullname, lastname, dni, id))
        mysql.connection.commit()
        flash('CONTACTO ACTUALIZADO')
        return redirect(url_for('Index'))



if __name__ == '__main__':
    app.run(port=3000, debug=True)
