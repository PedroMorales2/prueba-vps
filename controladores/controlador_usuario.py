from controladores.bd import conectar

def login(username, password):
    connection = conectar()
    with connection.cursor() as cursor:
        sql = "SELECT * FROM usuarios WHERE nombre = %s AND contrasena = %s"
        cursor.execute(sql, (username, password))
        result = cursor.fetchone()
    connection.close()
    return result
