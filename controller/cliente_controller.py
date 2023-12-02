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
    print(cliente)
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

def validarEmail(email):
    
    all_productos = Cliente.query.where(Cliente.email == email)  # Obtiene todos los registros de la tabla 
    result = clientes_schema.dump(all_productos)  # Serializa los registros en formato JSON    
    
    if len(result) <= 0:
        return  jsonify({"datos":False, "MSG":"correo electronico inexistente", "CODIGO":000})

    return  jsonify({"datos":True, "MSG":"correo electronico Ok", "CODIGO":200}) # Retorna msj de confirmacion

    # return  jsonify({"datos":result, "MSG":"correo ok", "CODIGO":200}) # Retorna los datos del cliente especifico al email y un mensaje
	
def validarLogin(email, clave):
    
    all_productos = Cliente.query.where(Cliente.email == email , Cliente.clave == clave)
    result = clientes_schema.dump(all_productos)  # Serializa los registros en formato JSON    
    
    if len(result) <= 0:
        return  jsonify({"datos":False, "MSG":"clave inexistente o erronea", "CODIGO":000})

    return  jsonify({"datos":True, "MSG":"correo electronico Ok", "CODIGO":200}) # Retorna msj de confirmacion

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