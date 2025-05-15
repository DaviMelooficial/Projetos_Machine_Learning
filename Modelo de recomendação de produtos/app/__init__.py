from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes.recomendacao import recomendacao_bp
    app.register_blueprint(recomendacao_bp)
    from app.routes.cliente import cliente_bp
    app.register_blueprint(cliente_bp)
    
    return app