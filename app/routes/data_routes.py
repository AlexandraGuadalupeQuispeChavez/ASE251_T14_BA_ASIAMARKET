"""
Rutas para consultar datos de las colecciones de MongoDB
"""
from flask import Blueprint, jsonify, request
from app.database.mongodb import get_database
from bson import ObjectId

data_bp = Blueprint("data", __name__, url_prefix="/api/data")

def serialize_doc(doc):
    """Convierte ObjectId a string para serialización JSON"""
    if doc and '_id' in doc:
        doc['_id'] = str(doc['_id'])
    return doc

# ==========================================
# RUTAS PARA CATEGORÍAS
# ==========================================
@data_bp.route("/categories", methods=["GET"])
def get_categories():
    """Obtiene todas las categorías"""
    try:
        db = get_database()
        categories = list(db.categories.find())
        categories = [serialize_doc(cat) for cat in categories]
        
        return jsonify({
            "success": True,
            "total": len(categories),
            "data": categories
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@data_bp.route("/categories/<category_id>", methods=["GET"])
def get_category_by_id(category_id):
    """Obtiene una categoría por ID"""
    try:
        db = get_database()
        category = db.categories.find_one({"category_id": category_id})
        
        if category:
            return jsonify({
                "success": True,
                "data": serialize_doc(category)
            }), 200
        else:
            return jsonify({
                "success": False,
                "message": "Categoría no encontrada"
            }), 404
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# ==========================================
# RUTAS PARA PRODUCTOS
# ==========================================
@data_bp.route("/products", methods=["GET"])
def get_products():
    """Obtiene todos los productos con paginación"""
    try:
        db = get_database()
        
        # Parámetros de paginación
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
        skip = (page - 1) * limit
        
        # Obtener productos
        products = list(db.products.find().skip(skip).limit(limit))
        products = [serialize_doc(prod) for prod in products]
        
        # Total de documentos
        total = db.products.count_documents({})
        
        return jsonify({
            "success": True,
            "page": page,
            "limit": limit,
            "total": total,
            "total_pages": (total + limit - 1) // limit,
            "data": products
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@data_bp.route("/products/<product_id>", methods=["GET"])
def get_product_by_id(product_id):
    """Obtiene un producto por ID"""
    try:
        db = get_database()
        product = db.products.find_one({"product_id": product_id})
        
        if product:
            return jsonify({
                "success": True,
                "data": serialize_doc(product)
            }), 200
        else:
            return jsonify({
                "success": False,
                "message": "Producto no encontrado"
            }), 404
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# ==========================================
# RUTAS PARA CLIENTES
# ==========================================
@data_bp.route("/customers", methods=["GET"])
def get_customers():
    """Obtiene todos los clientes con paginación"""
    try:
        db = get_database()
        
        # Parámetros de paginación
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
        skip = (page - 1) * limit
        
        # Obtener clientes
        customers = list(db.customers.find().skip(skip).limit(limit))
        customers = [serialize_doc(cust) for cust in customers]
        
        # Total de documentos
        total = db.customers.count_documents({})
        
        return jsonify({
            "success": True,
            "page": page,
            "limit": limit,
            "total": total,
            "total_pages": (total + limit - 1) // limit,
            "data": customers
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@data_bp.route("/customers/<customer_id>", methods=["GET"])
def get_customer_by_id(customer_id):
    """Obtiene un cliente por ID"""
    try:
        db = get_database()
        customer = db.customers.find_one({"customer_id": customer_id})
        
        if customer:
            return jsonify({
                "success": True,
                "data": serialize_doc(customer)
            }), 200
        else:
            return jsonify({
                "success": False,
                "message": "Cliente no encontrado"
            }), 404
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# ==========================================
# RUTAS PARA VENTAS
# ==========================================
@data_bp.route("/sales", methods=["GET"])
def get_sales():
    """Obtiene todas las ventas con paginación"""
    try:
        db = get_database()
        
        # Parámetros de paginación
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
        skip = (page - 1) * limit
        
        # Obtener ventas
        sales = list(db.sales.find().skip(skip).limit(limit))
        sales = [serialize_doc(sale) for sale in sales]
        
        # Total de documentos
        total = db.sales.count_documents({})
        
        return jsonify({
            "success": True,
            "page": page,
            "limit": limit,
            "total": total,
            "total_pages": (total + limit - 1) // limit,
            "data": sales
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@data_bp.route("/sales/<sale_id>", methods=["GET"])
def get_sale_by_id(sale_id):
    """Obtiene una venta por ID"""
    try:
        db = get_database()
        sale = db.sales.find_one({"sale_id": sale_id})
        
        if sale:
            return jsonify({
                "success": True,
                "data": serialize_doc(sale)
            }), 200
        else:
            return jsonify({
                "success": False,
                "message": "Venta no encontrada"
            }), 404
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@data_bp.route("/sales/by-date-range", methods=["GET"])
def get_sales_by_date_range():
    """
    Obtiene ventas filtradas por rango de fechas
    Parámetros: start_date (YYYY-MM-DD), end_date (YYYY-MM-DD)
    """
    try:
        db = get_database()
        
        # Obtener parámetros de fecha
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        
        if not start_date or not end_date:
            return jsonify({
                "success": False,
                "message": "Se requieren los parámetros 'start_date' y 'end_date' en formato YYYY-MM-DD"
            }), 400
        
        # Construir query
        query = {
            "date": {
                "$gte": start_date,
                "$lte": end_date
            }
        }
        
        # Obtener ventas en el rango
        sales = list(db.sales.find(query))
        sales = [serialize_doc(sale) for sale in sales]
        
        # Calcular estadísticas
        total_sales = len(sales)
        total_amount = sum(sale.get('total_amount', 0) for sale in sales)
        
        return jsonify({
            "success": True,
            "start_date": start_date,
            "end_date": end_date,
            "total_sales": total_sales,
            "total_amount": total_amount,
            "data": sales
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@data_bp.route("/sales/by-product", methods=["GET"])
def get_sales_by_product():
    """
    Obtiene el total de ventas agrupadas por producto
    Muestra cantidad vendida y monto total por cada producto
    """
    try:
        db = get_database()
        
        # Agregación para sumar ventas por producto
        pipeline = [
            {
                "$group": {
                    "_id": "$product_id",
                    "product_name": {"$first": "$product_name"},
                    "total_quantity": {"$sum": "$quantity"},
                    "total_amount": {"$sum": "$total_amount"},
                    "total_sales": {"$sum": 1}
                }
            },
            {
                "$sort": {"total_amount": -1}  # Ordenar por monto total descendente
            }
        ]
        
        results = list(db.sales.aggregate(pipeline))
        
        # Serializar resultados
        for item in results:
            item['product_id'] = item.pop('_id')
        
        return jsonify({
            "success": True,
            "total_products": len(results),
            "data": results
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# ==========================================
# RUTA DE ESTADÍSTICAS GENERALES
# ==========================================
@data_bp.route("/stats", methods=["GET"])
def get_stats():
    """Obtiene estadísticas generales de todas las colecciones"""
    try:
        db = get_database()
        
        stats = {
            "categories": db.categories.count_documents({}),
            "products": db.products.count_documents({}),
            "customers": db.customers.count_documents({}),
            "sales": db.sales.count_documents({})
        }
        
        return jsonify({
            "success": True,
            "data": stats
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
