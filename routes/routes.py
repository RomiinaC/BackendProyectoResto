from controller.cliente_controller import *

app.get("/")(holaMundo)

app.post("/api/login")(validarLogin)

app.post("/api/login/new-user")(create_new_user)

app.get("/api/login/perfil/<email>")(mostrar_perfil)

app.delete("/api/login/perfil/<email>")(delete_user)

app.put("/api/login/perfil")(update_clave)