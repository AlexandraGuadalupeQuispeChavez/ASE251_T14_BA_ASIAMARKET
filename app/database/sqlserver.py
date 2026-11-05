import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración de SQL Server
SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_USERNAME = os.getenv("SQL_USERNAME")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")
SQL_DRIVER = os.getenv("SQL_DRIVER", "{ODBC Driver 17 for SQL Server}")


def get_connection():
    """
    Crea y retorna una nueva conexión a SQL Server.
    Nota: El llamador es responsable de cerrar la conexión.
    """
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
            f"PWD={SQL_PASSWORD};"
            f"TrustServerCertificate=yes;"
        )
        
        connection = pyodbc.connect(connection_string)
        return connection
        
    except ImportError:
        raise ImportError(
            "❌ Error: pyodbc no está instalado.\n"
            "Instala pyodbc con: pip install pyodbc"
        )
    except Exception as e:
        raise ConnectionError(f"❌ Error al conectar a SQL Server: {e}")
