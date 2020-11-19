import eel
import pyodbc
from hashlib import sha256

@eel.expose 
def validarEntrada(usuario, contraseña):
    contraseñaHash = sha256(contraseña.encode('utf-8')).hexdigest()

    conn = pyodbc.connect(r'Driver={SQL Server};' 
                    r'Server=LAPTOP-VUGPNFNP\SQLEXPRESS;'
                    r'Database=DB_datos;'
                    r'Trusted_Connection=yes;')

    query = f''' set nocount on;
                select Valido from [DB_datos].[dbo].[BDUsuario]
                where usuario = '{usuario}' and contraseña = '{contraseñaHash}' '''

    cursor = conn.cursor()
    cursor.execute(query)
    
    try:
        resultadoServidor = cursor.fetchall()[0][0]
        return resultadoServidor
    except IndexError:
        return 0

    