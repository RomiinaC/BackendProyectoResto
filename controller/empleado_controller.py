from app import app
from models.modelo import empleado_schema, empleados_schema, Empleado, db
from flask import  jsonify, request, send_from_directory
from werkzeug.utils import secure_filename
import os

def obtener_empleados():
    all_empleados = Empleado.query.all() 
    result = empleados_schema.dump(all_empleados)  
    if result: 
        return  jsonify({"empleados": result}) 
    else:
        return jsonify({'error': 'Lista de empleados no encontrada'}), 404

def obtener_empleado(id_empleado):
    empleado = Empleado.query.get(id_empleado)
    if empleado:
        return empleado_schema.jsonify(empleado) 
    else:
        return jsonify({'error': 'Empleado no encontrado'}), 404

def create_new_empleado():
    try:
        nombre = request.form["nombre"] 
        apellido = request.form["apellido"]  
        puesto = request.form["puesto"]  
        email = request.form["email"] 
        clave = request.form["clave"] 
        dni = request.form["dni"] 
        fecha_ingreso = request.form["fecha_ingreso"]
        salario = request.form["salario"]
        tel = request.form["tel"]
        direccion = request.form["direccion"]
        fecha_nac = request.form["fecha_nac"]
        id_restaurante = "1"

        new_empleado = Empleado(nombre, apellido,puesto, email, clave,dni, fecha_ingreso, salario,tel, direccion, fecha_nac, id_restaurante) 
        db.session.add(new_empleado) 
        db.session.commit() 
        return empleado_schema.jsonify(new_empleado)  # Retorna el JSON del nuevo cliente creado
    except Exception as e:
        return jsonify({"mensaje": f"Error {e}", "CODIGO": 404})

def update_empleado(id_empleado):
    try:
        empleado = Empleado.query.get(id_empleado) 

        empleado.nombre = request.form["nombre"] 
        empleado.apellido = request.form["apellido"] 
        empleado.puesto = request.form["puesto"]    
        empleado.email = request.form["email"] 
        empleado.clave = request.form["clave"]
        empleado.dni = request.form["dni"] 
        empleado.fecha_ingreso = request.form["fecha_ingreso"]
        empleado.salario = request.form["salario"]
        empleado.tel = request.form["tel"]
        empleado.direccion = request.form["direccion"]
        empleado.fecha_nac = request.form["fecha_nac"]
        empleado.id_restaurante = "1"

        db.session.commit()  
        return empleado_schema.jsonify(empleado) 
    except Exception as e:
        return jsonify({"mensaje": f"Error: {e}", "CODIGO": 404})

def delete_empleado(id_empleado):
    try:    
        empleado = Empleado.query.get(id_empleado)
        db.session.delete(empleado) 
        db.session.commit() 
        return empleado_schema.jsonify(empleado)  # Retorna el JSON del cliente eliminado
    except Exception as e:
        return jsonify({"mensaje": f"Error: {e}", "CODIGO": 404})