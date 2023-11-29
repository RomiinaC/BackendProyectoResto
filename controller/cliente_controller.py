from app import app
from models.modelo import cliente_schema, clientes_schema, Cliente, db
from flask import  jsonify, request

# Ruta de prueba
# @app.route("/")
def holaMundo():
    return "<h1>Hello World</h1>"

#Obtiene todos los clientes
#  @app.route("/clientes", methods=["GET"])
def get_clientes():

    all_productos = Cliente.query.all()  # Obtiene todos los registros de la tabla 
    result = clientes_schema.dump(all_productos)  # Serializa los registros en formato JSON    
    return  jsonify(result) # Retorna el JSON de todos los registros de la tabla

#Obtiene un cliente por id
# @app.route("/clientes/<id_cliente>", methods=["GET"])
def get_cliente_por_id(id_cliente):
    
    cliente = Cliente.query.get(id_cliente)  # Obtiene el cliente correspondiente al ID recibido
    return cliente_schema.jsonify(cliente)  # Retorna el JSON del cliente

#Elimina a un cliente por id
# @app.route("/clientes/<id_cliente>", methods=["DELETE"])
def delete_cliente_por_id(id_cliente):

    cliente = Cliente.query.get(id_cliente)
    db.session.delete(cliente)  # Elimina el producto de la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    return cliente_schema.jsonify(cliente)  # Retorna el JSON del cliente eliminado

#Crea un nuevo cliente
# @app.route("/clientes", methods=["POST"])
def create_cliente():
    
    nombre = request.json["nombre"] 
    apellido = request.json["apellido"]  
    clave = request.json["clave"]  
    email = request.json["email"] 
    fecha_nac = request.json["fecha_nac"]
    tel = request.json["tel"]
    id_restaurante = request.json["id_restaurante"]

    new_cliente = Cliente(nombre, apellido, clave, email, fecha_nac, tel, id_restaurante) 
    db.session.add(new_cliente)  # Agrega el nuevo cliente a la sesión de la base de datos
    db.session.commit() 
    return cliente_schema.jsonify(new_cliente)  # Retorna el JSON del nuevo cliente creado

#Actualiza todos los datos de un cliente por id
# @app.route("/clientes/<id_cliente>", methods=["PUT"])  
def update_cliente(id_cliente):
 
    cliente = Cliente.query.get(id_cliente) 

    # Actualiza los atributos con los datos proporcionados en el JSON
    cliente.nombre = request.json["nombre"] 
    cliente.apellido = request.json["apellido"]  
    cliente.clave = request.json["clave"]  
    cliente.email = request.json["email"] 
    cliente.fecha_nac = request.json["fecha_nac"]
    cliente.tel = request.json["tel"]
    cliente.id_restaurante = request.json["id_restaurante"]

    db.session.commit()  
    return cliente_schema.jsonify(cliente)  # Retorna el JSON del producto actualizado
