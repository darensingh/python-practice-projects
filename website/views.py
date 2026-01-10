from flask import Blueprint, render_template

print(">>> Python is reading the correct views.py file!")

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")