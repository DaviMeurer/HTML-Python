from .usuario_routes import usuario_bp

def iniciar_rotas(app):
    app.register_blueprint(usuario_bp)