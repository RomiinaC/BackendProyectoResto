from app import app
from models.modelo import cliente_schema, clientes_schema, Cliente, db, Empleado
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
            return  jsonify({"datos":False, "mensaje":"Error! No se encuentra usuario", "CODIGO":204})

        return  jsonify({"datos":True, "mensaje":"Inicio de sesion exitoso", "CODIGO":200}) # Retorna msj de confirmacion
    except Exception as e:
        return jsonify({"datos":False, "mensaje":"Error en el inicio de sesion", "CODIGO":404})

def create_new_user():
    try:
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
    except Exception as e:
        return f"Error: {e}"

def mostrar_perfil(email):
    try:
        all_productos = Cliente.query.where(Cliente.email == email)  # Obtiene todos los registros de la tabla 
        result = clientes_schema.dump(all_productos)
        return jsonify(result)
    except Exception as e:
        return f"Error {e}"

def delete_user(email):
    try:
        all_clientes = Cliente.query.filter(Cliente.email == email)
        all_clientes.delete()
        db.session.commit()
        return jsonify({"mensaje":"Usuario eliminado exitosamente", "CODIGO":200, "complete":True})
    except Exception as e:
        return jsonify({"mensaje":"Error al eliminar usuario", "CODIGO":404, "complete":False})
    
def update_clave():
    try:    
        email = request.json["email"] 
        all_clientes = Cliente.query.filter(Cliente.email == email) 
        cliente = all_clientes[0]
        cliente.clave = request.json["clave"]  
        # cliente.tel = request.json["tel"] 
        #Busca el mail del cliente a modificar en la tabla empleado
        all_empleados = Empleado.query.filter(Empleado.email == email)
        empleado = all_empleados[0]
        #Comprueba si el empleado a modificar es administrador
        if empleado.puesto == "ADM":
            empleado.clave = request.json["clave"] 
            print(empleado)
        db.session.commit() 
        print(cliente) 
        return jsonify({"mensaje":"Usuario actualizado exitosamente", "CODIGO":200, "complete":True})
    except Exception as e:
        return jsonify({"mensaje":f"Error {e}", "CODIGO":404, "complete":False})

def update_cliente(id_empleado):
    try:
        empleado = Empleado.query.get(id_empleado)
        all_clientes = Cliente.query.filter(Cliente.email == empleado.email) 
        cliente = all_clientes[0]

        cliente.nombre = request.json["nombre"] 
        cliente.apellido = request.json["apellido"]  
        cliente.clave = request.json["clave"]  
        cliente.fecha_nac = request.json["fecha_nac"]
        cliente.tel = request.json["tel"]
        cliente.id_restaurante = "1"
        cliente.email = request.json["email"] 

        db.session.commit() 
    
        return jsonify({"mensaje":"Usuario actualizado exitosamente", "CODIGO":200, "complete":True})
    
    except Exception as e:
        return jsonify({"mensaje":f"Error {e}", "CODIGO":404, "complete":False})