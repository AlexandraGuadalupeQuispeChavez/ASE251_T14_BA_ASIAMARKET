"""
Repositorio para operaciones con SQL Server - Sales
"""
from app.database.sqlserver import get_connection as get_sqlserver_connection


class SQLServerSalesRepository:
    """
    Repositorio que gestiona las consultas SQL contra la tabla sales
    """

    def get_total_sales(self, year=None, month=None):
        """
        Obtiene el total de ventas con filtros opcionales de año y mes
        
        Args:
            year (int, optional): Año para filtrar las ventas
            month (int, optional): Mes para filtrar las ventas (1-12)
        
        Returns:
            float: Total de ventas según los filtros aplicados
        """
        query = """
            SELECT COALESCE(SUM(total_amount), 0)
            FROM sales
        """
        
        conditions = []
        params = []
        
        if year is not None:
            conditions.append("YEAR(sale_date) = ?")
            params.append(year)
        
        if month is not None:
            conditions.append("MONTH(sale_date) = ?")
            params.append(month)
        
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        
        connection = get_sqlserver_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute(query, params)
            result = cursor.fetchone()
            # Convertir Decimal a float para facilitar
            # la serialización JSON en Flask.
            return float(result[0] or 0)
        finally:
            cursor.close()
            connection.close()
