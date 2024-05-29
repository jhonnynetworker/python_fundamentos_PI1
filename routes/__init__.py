# routes/__init__.py
from .auth_routes import auth_bp
from .product_routes import product_bp, register_product_routes
from .purchase_routes import purchase_bp, register_purchase_routes

# Registra las rutas usando los Blueprint
register_product_routes(product_bp)
register_purchase_routes(purchase_bp)
