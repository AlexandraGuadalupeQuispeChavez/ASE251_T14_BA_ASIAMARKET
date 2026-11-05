"""
Servicio analítico para cálculo de indicadores de ventas
"""
from app.repositories.sqlserver.sales_repository import SQLServerSalesRepository
from app.schemas.sales_schema import IndicatorResponse


class AnalyticsService:
    """
    Servicio que contiene la lógica analítica para transformar
    datos de ventas en indicadores empresariales
    """
    
    def __init__(self):
        self.repository = SQLServerSalesRepository()
    
    def total_sales(self, year=None, month=None):
        """
        Calcula el monto total de ventas con filtros opcionales
        
        Args:
            year (int, optional): Año para filtrar las ventas
            month (int, optional): Mes para filtrar las ventas
        
        Returns:
            IndicatorResponse: Objeto con el indicador de ventas totales
        """
        result = self.repository.get_total_sales(
            year=year,
            month=month
        )
        
        return IndicatorResponse(
            indicator="sales_total",
            title="Ventas Totales",
            chart_type="card",
            data=result,
            sources=["SQL Server"]
        )
