from app import app
from models.modelo import plato_schema, platos_schema, Plato, db
from flask import  jsonify, request, send_from_directory
from werkzeug.utils import secure_filename
import os

app.config['FOLDER_IMG_MENU'] = 'public/img/platos'

def mostrar_menu():
    all_productos = Plato.query.all()  # Obtiene todos los registros de la tabla 
    result = platos_schema.dump(all_productos)  # Serializa los registros en formato JSON    
    return  jsonify(result) # Retorna el JSON de todos los registros de la tabla

def categorias(cat):
    try:
        cat_platos= Plato.query.filter(Plato.categoria == cat).all()
        c_platos = platos_schema.dump(cat_platos)
        if c_platos:
            return jsonify(c_platos)
        else: 
             return jsonify({"MSG":"Categoria no encontrada", "CODIGO":000, "complete":False}),404

    except Exception as e: 
        return jsonify({f"MSG":"Error {e}", "CODIGO":000, "complete":False})

def obtener_img_plato_por_id(filename):
    return send_from_directory(app.config['FOLDER_IMG_MENU'], filename)

def crear_plato():

    nombre = request.form['nombre']
    categoria = request.form['categoria']
    tipo = request.form['tipo']
    foto = request.files['foto']
    id_menu = request.form['id_menu']
    precio = request.form['precio']
    
    print(request.url)

    # Toma el nombre del archivo original como entrada y devuelve un nombre de archivo seguro para su almacenamiento.
    nombre_imagen = secure_filename(foto.filename)
    # Separa el nombre del archivo de su extensión, considerando el punto como separador.
    nombre_base, extension = os.path.splitext(nombre_imagen)
    # Guarda la imagen con el nombre asociado a su ID.
    nombre_imagen = f"{nombre_base}{extension}"
    foto.save(os.path.join(app.config['FOLDER_IMG_MENU'], nombre_imagen))

    new_plato = Plato(nombre, categoria, tipo,f"/{app.config['PATH_IMG_MENU']}/{nombre_imagen}" , id_menu, precio) 
    db.session.add(new_plato)  # Agrega el nuevo cliente a la sesión de la base de datos
    db.session.commit() 
    
    return jsonify(new_plato), 201