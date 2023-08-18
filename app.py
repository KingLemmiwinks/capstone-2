import os
from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db

# API_BASE_URL = "https://www.dnd5eapi.co/api"
# CURR_USER_KEY = "curr_user"

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///capstone_2_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.drop_all()
db.create_all()


############################## HOME ROUTE ##############################


@app.route('/')

def home():
    """Show home page."""

    return render_template('index.html')