import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración de SQL Server (para uso futuro)
SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_USERNAME = os.getenv("SQL_USERNAME")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")
SQL_DRIVER = os.getenv("SQL_DRIVER", "{ODBC Driver 17 for SQL Server}")

# Variables globales
connection = None

def get_connection():
    """
    Obtiene la conexión a SQL Server.
    Nota: Requiere pyodbc instalado y configurado.
    """
    global connection
    
    if connection is None:
        # Validar configuración
        if not all([SQL_SERVER, SQL_DATABASE, SQL_USERNAME, SQL_PASSWORD]):
            raise ValueError(
                "❌ Error: Variables de SQL Server no configuradas.\n"
                "Por favor configura SQL_SERVER, SQL_DATABASE, SQL_USERNAME y SQL_PASSWORD en el archivo .env"
            )
        
        try:
            import pyodbc
            
            connection_string = (
                f"DRIVER={SQL_DRIVER};"
                f"SERVER={SQL_SERVER};"
                f"DATABASE={SQL_DATABASE};"
                f"UID={SQL_USERNAME};"
                f"PWD={SQL_PASSWORD}"
            )
            
            connection = pyodbc.connect(connection_string)
            print("✅ Conexión exitosa a SQL Server")
            
        except ImportError:
            raise ImportError(
                "❌ Error: pyodbc no está instalado.\n"
                "Instala pyodbc con: pip install pyodbc"
            )
        except Exception as e:
            raise ConnectionError(f"❌ Error al conectar a SQL Server: {e}")
    
    return connection

def close_connection():
    """Cierra la conexión a SQL Server"""
    global connection
    if connection:
        connection.close()
        connection = None
        print("✅ Conexión a SQL Server cerrada")

def execute_query(query, params=None):
    """
    Ejecuta una consulta SQL y retorna los resultados.
    
    Args:
        query (str): Consulta SQL a ejecutar
        params (tuple, optional): Parámetros para la consulta
    
    Returns:
        list: Lista de resultados
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    
    if query.strip().upper().startswith("SELECT"):
        columns = [column[0] for column in cursor.description]
        results = []
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))
        return results
    else:
        conn.commit()
        return {"affected_rows": cursor.rowcount}

# Ejemplo de uso (descomentado cuando se necesite):
"""
# Agregar al archivo .env:
SQL_SERVER=tu-servidor.database.windows.net
SQL_DATABASE=tu-base-de-datos
SQL_USERNAME=tu-usuario
SQL_PASSWORD=tu-password
SQL_DRIVER={ODBC Driver 17 for SQL Server}

# Ejemplo de uso:
from app.database.sqlserver import execute_query

# SELECT
results = execute_query("SELECT * FROM tabla WHERE id = ?", (1,))

# INSERT
execute_query("INSERT INTO tabla (columna) VALUES (?)", ("valor",))
"""
