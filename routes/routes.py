from controller.cliente_controller import *
from controller.plato_controller import *
from controller.empleado_controller import *

# Establece ruta lógica del servidor que aloja las imágenes de los platos
app.config['PATH_IMG_MENU'] = 'api/menu/img'

app.get("/")(holaMundo)

# RUTAS PARA LOS USUARIOS
app.post("/api/login")(validarLogin)

app.post("/api/login/new-user")(create_new_user)

app.get("/api/login/perfil/<email>")(mostrar_perfil)

app.delete("/api/login/perfil/<email>")(delete_user)

app.put("/api/login/perfil")(update_clave)

# RUTAS PARA EL MENU
app.get("/api/menu")(mostrar_menu)

app.get("/api/menu/filter-c=<cat>")(categorias)

app.get(f"/{app.config['PATH_IMG_MENU']}/<filename>")(obtener_img_plato_por_id)

# app.post("/api/menu")


# RUTAS PARA ADMIN
app.get("/api/admin/empleados")(obtener_empleados)

app.get("/api/admin/empleados/<id_empleado>")(obtener_empleado)

app.post("/api/admin/empleados")(create_new_empleado)

app.put("/api/admin/empleados/<id_empleado>")(update_empleado)

app.delete("/api/admin/empleados/<id_empleado>")(delete_empleado)