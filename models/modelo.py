from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Configura la URI (Uniform Resource Identifier) de la base de datos con el driver de MySQL, usuario, contraseña y nombre de la base de datos. Esta configuración permite establecer la conexión con la base de datos.
# URI de la BD == Driver de la BD://user:password@UrlBD/nombreBD
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:k0707@localhost/resto"
# Configura el seguimiento de modificaciones de SQLAlchemy a False para mejorar el rendimiento
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Crea una instancia de la clase SQLAlchemy para interactuar con la base de datos. Este objeto proporciona métodos y funcionalidades para realizar consultas y operaciones en la base de datos.
db = SQLAlchemy(app)
# Crea una instancia de la clase Marshmallow para trabajar con serialización y deserialización de datos. Este objeto se utilizará para definir los esquemas de los modelos de datos en la aplicación.
ma = Marshmallow(app)


# tabla cliente

class Cliente(db.Model): 
    """
    Definición de la tabla Cliente en la base de datos.
    """
    id_cliente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    clave = db.Column(db.String(100))
    email = db.Column(db.String(100))
    fecha_nac = db.Column(db.Date())
    tel = db.Column(db.String(100))
    id_restaurante = db.Column(db.Integer)

    def __init__(self, nombre, apellido, clave, email, fecha_nac, tel, id_restaurante):
       
        self.nombre = nombre
        self.apellido = apellido
        self.clave = clave
        self.email = email
        self.fecha_nac = fecha_nac
        self.tel = tel
        self.id_restaurante = id_restaurante


class ClienteSchema(ma.Schema):
    
    class Meta:
        fields = ("id_cliente", "nombre", "apellido", "clave", "email","fecha_nac","tel","id_restaurante")

cliente_schema = ClienteSchema()  # Objeto para serializar/deserializar un producto
clientes_schema = ClienteSchema(many=True)  # Objeto para serializar/deserializar múltiples productos


# tabla plato
class Plato(db.Model): 
    """
    Definición de la tabla Plato en la base de datos.
    """
    id_plato = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    categoria = db.Column(db.String(100))
    tipo = db.Column(db.String(10))
    foto = db.Column(db.String(100))
    id_menu = db.Column(db.Integer)
    precio = db.Column(db.Integer)
    
    def __init__(self, nombre, categoria, tipo, foto, precio, id_menu):
       
        self.nombre = nombre
        self.categoria = categoria
        self.tipo =tipo
        self.foto = foto
        self.precio = precio
        self.id_menu = id_menu

class PlatoSchema(ma.Schema):   
    class Meta:
        fields = ("id_plato", "nombre", "categoria", "tipo", "foto","precio","id_menu")

plato_schema = PlatoSchema()  # Objeto para serializar/deserializar un producto
platos_schema = PlatoSchema(many=True)  # Objeto para serializar/deserializar múltiples productos

# tabla empleado
class Empleado(db.Model): 
    """
    Definición de la tabla Cliente en la base de datos.
    """
    id_empleado = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    puesto = db.Column(db.String(100))
    email = db.Column(db.String(100))
    clave = db.Column(db.String(100))
    dni = db.Column(db.String(100))
    fecha_ingreso = db.Column(db.Date())
    salario = db.Column(db.Integer)
    tel = db.Column(db.String(100))
    direccion = db.Column(db.String(100))
    fecha_nac = db.Column(db.Date())
    id_restaurante = db.Column(db.Integer)

    def __init__(self, nombre, apellido,puesto, email, clave, dni, fecha_ingreso, salario, tel, direccion, fecha_nac, id_restaurante):
       
        self.nombre = nombre
        self.apellido = apellido
        self.puesto = puesto
        self.email = email
        self.clave = clave
        self.dni = dni
        self.fecha_ingreso = fecha_ingreso
        self.salario = salario
        self.tel = tel
        self.direccion = direccion
        self.fecha_nac = fecha_nac
        self.id_restaurante = id_restaurante


class EmpleadoSchema(ma.Schema):
    
    class Meta:
        fields = ("id_empleado", "nombre", "apellido","puesto","email", "clave", "dni", "fecha_ingreso","salario","tel","direccion","fecha_nac", "id_restaurante")

empleado_schema = EmpleadoSchema()  # Objeto para serializar/deserializar un producto
empleados_schema = EmpleadoSchema(many=True)  # Objeto para serializar/deserializar múltiples productos



# Crea todas las tablas en la base de datos. Siempre al final del archivo
with app.app_context():
     db.create_all()  