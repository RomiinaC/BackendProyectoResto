from controller.cliente_controller import *

app.get("/")(holaMundo)

app.get("/clientes")(get_clientes)
app.get("/clientes/<id_cliente>")(get_cliente_por_id)

app.delete("/clientes/<id_cliente>")(delete_cliente_por_id)

app.post("/clientes")(create_cliente)

app.put("/clientes/<id_cliente>")(update_cliente)

app.get("/api/login/<email>")(validarEmail)

app.get("/api/login/<email>/<clave>")(validarLogin)

app.post("/api/login/new-user")(create_new_user)

app.get("/api/login/perfil/<email>")(mostrar_perfil)

app.delete("/api/login/perfil/<email>")(delete_user)