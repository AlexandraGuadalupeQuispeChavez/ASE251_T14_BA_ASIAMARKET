"""
Módulo de gestión de conexiones a bases de datos

Este módulo centraliza las conexiones a:
- MongoDB Atlas (Base de datos principal)
- SQL Server (Base de datos secundaria/futura)
"""

from .mongodb import get_database, close_connection as close_mongo_connection

# Exportar funciones principales
__all__ = [
    'get_database',
    'close_mongo_connection'
]

# Para SQL Server (descomenta cuando sea necesario):
# from .sqlserver import get_connection, close_connection as close_sql_connection, execute_query
# __all__.extend(['get_connection', 'close_sql_connection', 'execute_query'])
