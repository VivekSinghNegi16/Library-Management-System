from flask import Flask, g, escape, session, redirect, render_template, request, jsonify, Response
from Misc.functions import *

app = Flask(__name__)
app.secret_key = '#$ab9&^BB00_.'

from Models.DAO import DAO

DAO = DAO(app)


from routes.user import user_view
from routes.book import book_view
from routes.admin import admin_view


app.jinja_env.globals.update(
    ago=ago,
    str=str,
)

@app.route('/', methods=['GET'])
def index():
	return render_template('shared/layout.html')

app.register_blueprint(admin_view)
app.register_blueprint(user_view)
app.register_blueprint(book_view)
