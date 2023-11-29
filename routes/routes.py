from controller.cliente_controller import *

app.get("/")(holaMundo)

app.get("/clientes")(get_clientes)
app.get("/clientes/<id_cliente>")(get_cliente_por_id)

app.delete("/clientes/<id_cliente>")(delete_cliente_por_id)

app.post("/clientes")(create_cliente)

app.put("/clientes/<id_cliente>")(update_cliente)

app.get("/login/<email>")(validarEmail)

app.get("/login/<email>/<clave>")(validarLogin)