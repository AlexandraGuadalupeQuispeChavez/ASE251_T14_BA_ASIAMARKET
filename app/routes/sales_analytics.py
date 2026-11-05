"""
Rutas para servicios analíticos de ventas
"""
from flask import Blueprint, jsonify, request
from app.services.analytics.sales_service import AnalyticsService

analytics_bp = Blueprint(
    "analytics",
    __name__
)

service = AnalyticsService()


def get_date_filters():
    """
    Extrae y valida los parámetros year y month de la petición
    
    Returns:
        tuple: (year, month, error_response)
            - year: int o None
            - month: int o None
            - error_response: tupla (jsonify, status_code) o None si no hay errores
    """
    year_raw = request.args.get("year")
    month_raw = request.args.get("month")
    
    errors = []
    year = None
    month = None
    
    # Validar año
    if year_raw is not None:
        try:
            year = int(year_raw)
            if not 1 <= year <= 9999:
                errors.append(
                    "El año debe estar entre 1 y 9999"
                )
        except ValueError:
            errors.append(
                "El año debe ser un número entero"
            )
    
    # Validar mes
    if month_raw is not None:
        try:
            month = int(month_raw)
            if not 1 <= month <= 12:
                errors.append(
                    "El mes debe estar entre 1 y 12"
                )
        except ValueError:
            errors.append(
                "El mes debe ser un número entero"
            )
    
    # Devolver todos los errores encontrados
    if errors:
        return None, None, (
            jsonify({
                "message": "Error en los parámetros enviados",
                "errors": errors
            }),
            400
        )
    
    return year, month, None


@analytics_bp.route(
    "/analytics/sales-total",
    methods=["GET"]
)
def sales_total():
    """
    Endpoint para obtener el total de ventas con filtros opcionales
    
    Query Parameters:
        year (int, optional): Año para filtrar las ventas
        month (int, optional): Mes para filtrar las ventas (1-12)
    
    Returns:
        JSON con el indicador de ventas totales o mensaje de error
    """
    year, month, error = get_date_filters()
    if error:
        return error
    
    result = service.total_sales(
        year=year,
        month=month
    )
    
    return jsonify(result.__dict__)
