import pymysql.cursors

# Connect to the database
# def conectar():
#     return pymysql.connect(host='18.216.182.173',
#                              user='pedro1',
#                              password='Pedro@1234Xyz!',
#                              database='pruebas',
#                              cursorclass=pymysql.cursors.DictCursor)

def conectar():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                database='pruebas',
                                cursorclass=pymysql.cursors.DictCursor)