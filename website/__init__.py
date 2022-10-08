from flask import Flask

def create_app():
    # criando a funçao para iniciar o app
    
    app = Flask(__name__)
    # para as aplicacoes flask, criamos uma senha para encriptar os dados da aplicacao
    app.config['SECRET_KEY'] = 'something anything'
    
    from .views import views
    from .auth import auth
    
    # registrando as blueprints
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')
    return app