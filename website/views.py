from flask import Blueprint, render_template

# definindo a blueprint
views = Blueprint('views', __name__)

# definindo a rota da homepage
@views.route('/')
def home():
    return render_template("home.html")