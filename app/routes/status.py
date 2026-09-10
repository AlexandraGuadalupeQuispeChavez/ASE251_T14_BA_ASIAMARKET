from flask import Blueprint, jsonify

status_bp = Blueprint("status", __name__)

@status_bp.route("/")
def inicio():
    return jsonify({
        "estado": "Operativo",
        "servicio": "Backend Analítico",
        "mensaje": "API funcionando correctamente 🚀",
        "documentacion": {
            "swagger_ui": "http://127.0.0.1:5000/api/docs",
            "descripcion": "Interfaz interactiva para probar todos los endpoints"
        },
        "endpoints_disponibles": {
            "status": "/",
            "estadisticas": "/api/data/stats",
            "categorias": {
                "todas": "/api/data/categories",
                "por_id": "/api/data/categories/{category_id}"
            },
            "productos": {
                "todos": "/api/data/products?page=1&limit=10",
                "por_id": "/api/data/products/{product_id}"
            },
            "clientes": {
                "todos": "/api/data/customers?page=1&limit=10",
                "por_id": "/api/data/customers/{customer_id}"
            },
            "ventas": {
                "todas": "/api/data/sales?page=1&limit=10",
                "por_id": "/api/data/sales/{sale_id}"
            }
        }
    })
