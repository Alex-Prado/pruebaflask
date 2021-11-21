

from flask import Flask, render_template
import pymysql


app = Flask(__name__)


@app.route('/')
def Index():
    conectar = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='usuario'
    )
    cursor = conectar.cursor()
    cursor.execute('SELECT * FROM contacto')
    data = cursor.fetchall()

    return render_template('/index.html', contactos=data)


if __name__ == '__main__':
    app.run(port=300, debug=True)
