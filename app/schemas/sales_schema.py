"""
Esquemas de validación para ventas y respuestas analíticas
"""


class IndicatorResponse:
    """
    Formato estándar de respuesta para indicadores analíticos
    """
    
    def __init__(self, indicator, title, chart_type, data, sources):
        """
        Inicializa un objeto de respuesta de indicador
        
        Args:
            indicator (str): Identificador del indicador
            title (str): Título descriptivo del indicador
            chart_type (str): Tipo de visualización (card, bar, line, etc.)
            data: Dato o datos del indicador (puede ser número, lista, etc.)
            sources (list): Lista de fuentes de datos utilizadas
        """
        self.indicator = indicator
        self.title = title
        self.chart_type = chart_type
        self.data = data
        self.sources = sources
