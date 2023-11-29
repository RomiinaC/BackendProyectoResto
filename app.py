from flask import Flask, jsonify, request
from flask_cors import CORS

# Crea una instancia de la clase Flask con el nombre de la aplicación. El parámetro __name__ es una variable que representa el nombre del módulo o paquete en el que se encuentra este código (ubicación de los recursos de la aplicación)
app = Flask(__name__)
# Configura CORS para permitir el acceso desde el frontend al backend. Se utiliza el módulo CORS para habilitar el acceso cruzado entre dominios en la aplicación Flask.
CORS(app)


from routes.routes import *


'''
Este código es el programa principal de la aplicación Flask. Se verifica si el archivo actual está siendo ejecutado directamente y no importado como módulo. Luego, se inicia el servidor Flask en el puerto 5000 con el modo de depuración habilitado. Esto permite ejecutar la aplicación y realizar pruebas mientras se muestra información adicional de depuración en caso de errores.

'''
# Programa Principal
if __name__ == "__main__":

    app.run(debug=True, port=5000)

