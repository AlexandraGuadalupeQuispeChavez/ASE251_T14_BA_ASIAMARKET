from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Obtener configuración
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DATABASE = os.getenv("MONGO_DATABASE")

# Variables globales
client = None
db = None

def get_database():
    """
    Obtiene la conexión a la base de datos MongoDB.
    Si no existe conexión, la crea.
    """
    global client, db
    
    if client is None:
        # Validar que las variables de entorno estén configuradas
        if not MONGO_URI or not MONGO_DATABASE:
            raise ValueError(
                "❌ Error: Variables de entorno no configuradas.\n"
                "Por favor configura MONGO_URI y MONGO_DATABASE en el archivo .env"
            )
        
        # Validar que no sea la URI de ejemplo
        if "<username>" in MONGO_URI or "xxxxx" in MONGO_URI:
            raise ValueError(
                "❌ Error: El archivo .env contiene valores de ejemplo.\n"
                "Por favor reemplaza <username>, <password> y xxxxx con tus credenciales reales de MongoDB Atlas."
            )
        
        # Crear conexión
        client = MongoClient(MONGO_URI)
        db = client[MONGO_DATABASE]
        
        # Verificar conexión (ping)
        client.admin.command('ping')
    
    return db

def close_connection():
    """Cierra la conexión a MongoDB"""
    global client
    if client:
        client.close()
        client = None
