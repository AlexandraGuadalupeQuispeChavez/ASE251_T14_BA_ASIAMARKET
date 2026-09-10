"""
Repository para operaciones con la colección sales de MongoDB
"""
from app.database.mongodb import get_database

class SalesRepository:
    """
    Repositorio para acceder a los datos de ventas en MongoDB
    """
    
    def get_all_sales(self):
        """
        Obtiene todas las ventas de MongoDB
        
        Returns:
            list: Lista de todas las ventas
        """
        db = get_database()
        collection = db["sales"]
        return list(collection.find())
