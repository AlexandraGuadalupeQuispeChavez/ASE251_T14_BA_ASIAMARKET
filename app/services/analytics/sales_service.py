"""
Servicio analítico para cálculo de indicadores de ventas
"""
from app.repositories.mongodb.sales_repository import SalesRepository

class AnalyticsService:
    """
    Servicio que contiene la lógica analítica para transformar
    datos de ventas en indicadores empresariales
    """
    
    def __init__(self):
        self.repository = SalesRepository()
    
    def calculate_total_sales(self):
        """
        Calcula el monto total de todas las ventas
        
        Transforma: Datos de MongoDB → Indicador empresarial
        
        Returns:
            dict: Indicador con el monto total de ventas
        """
        # Obtener todas las ventas desde MongoDB
        sales = self.repository.get_all_sales()
        
        # Calcular el total sumando el campo total_amount
        total = 0
        for sale in sales:
            total += sale["total_amount"]
        
        # Retornar el indicador empresarial
        return {
            "indicator_name": "Total Sales",
            "total_sales": total,
            "currency": "PEN"
        }
