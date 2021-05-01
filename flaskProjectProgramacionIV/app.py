from flask import Flask, render_template, request, flash, jsonify
from flask_bootstrap import Bootstrap
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
Bootstrap(app)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        form_name = request.form['form-name']
        if form_name == "añadir":
            null = None
            title = request.form["title"]
            author = request.form["author"]
            anio = request.form["año"]
            lang = request.form["lenguaje"]
            pais = request.form["pais"]
            link = request.form["link"]
            nuevo = {
                "author": author,
                "country": pais,
                "imageLink": null,
                "language": lang,
                "link": link,
                "pages": null,
                "title": title,
                "year": int(anio)
            }
            datos = json.load(open('data/datos.json', 'r'))
            libros = datos["books"]
            libros.insert(0, nuevo)
            datos["books"] = libros
            json.dump(datos, open('data/datos.json', 'w'), indent=4)
            flash('Libro añadido correctamente!!! :)')

        elif form_name == "delete":
            index = int(request.form["number"])
            datos = json.load(open('data/datos.json', 'r'))
            libros = datos["books"]
            libros.pop(index)
            datos["books"] = libros
            json.dump(datos, open('data/datos.json', 'w'), indent=4)
            flash("Libro eliminado!!")

    datos = json.load(open('data/datos.json', 'r'))
    datos = datos["books"]

    return render_template('tablaDeDatos.html', len=len(datos), Datos=datos)


if __name__ == '__main__':
    app.run(host='192.168.0.138', threaded=True)
