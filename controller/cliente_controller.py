from app import app
from models.modelo import cliente_schema, clientes_schema, Cliente, db
from flask import  jsonify, request

# Ruta de prueba
# @app.route("/")
def holaMundo():
    return "<h1>Hello World</h1>"

def validarLogin():
    try:
        email = request.json["email"]
        clave = request.json["clave"]
        all_productos = Cliente.query.where(Cliente.email == email , Cliente.clave == clave)
        result = clientes_schema.dump(all_productos)  # Serializa los registros en formato JSON    
        
        if len(result) <= 0:
            return  jsonify({"datos":False, "MSG":"Error! No se encuentra usuario", "CODIGO":000})

        return  jsonify({"datos":True, "MSG":"Inicio de sesion exitoso", "CODIGO":200}) # Retorna msj de confirmacion
    except Exception as e:
        return jsonify({"datos":False, "MSG":"Error en el inicio de sesion", "CODIGO":000})


def create_new_user():

    nombre = request.json["nombre"] 
    apellido = request.json["apellido"]  
    clave = request.json["clave"]  
    email = request.json["email"] 
    fecha_nac = request.json["fecha_nac"]
    tel = request.json["tel"]
    id_restaurante = "1"

    new_cliente = Cliente(nombre, apellido, clave, email, fecha_nac, tel, id_restaurante) 
    db.session.add(new_cliente)  # Agrega el nuevo cliente a la sesión de la base de datos
    db.session.commit() 
    return cliente_schema.jsonify(new_cliente)  # Retorna el JSON del nuevo cliente creado

def mostrar_perfil(email):
    
    all_productos = Cliente.query.where(Cliente.email == email)  # Obtiene todos los registros de la tabla 
    result = clientes_schema.dump(all_productos)
    return jsonify(result)

def delete_user(email):

    all_clientes = Cliente.query.filter(Cliente.email == email)
    all_clientes.delete()
    db.session.commit()
    return jsonify({"MSG":"Usuario eliminado exitosamente", "CODIGO":200, "complete":True})

def update_clave():
    email = request.json["email"] 
    all_clientes = Cliente.query.filter(Cliente.email == email) 
    cliente = all_clientes[0]
    # Actualiza los atributos con los datos proporcionados en el JSON  
    # cliente.nombre = request.json["nombre"] 
    # cliente.apellido = request.json["apellido"]  
    cliente.clave = request.json["clave"]  
    # cliente.email = request.json["email"] 
    # cliente.fecha_nac = request.json["fecha_nac"]
    # cliente.tel = request.json["tel"]
    # cliente.id_restaurante = request.json["id_restaurante"]  
    db.session.commit() 
    print(cliente) 
    return jsonify({"MSG":"Usuario actualizado exitosamente", "CODIGO":200, "complete":True})