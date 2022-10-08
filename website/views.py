from flask import Blueprint

# definindo a blueprint
views = Blueprint('views', __name__)

# definindo a rota da homepage
@views.route('/')
def home():
    return "<h1>Test<h1>"