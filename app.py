import os
from flask import Flask, render_template, session, flash, redirect, g
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User
from forms import RegisterForm, LoginForm
from sqlalchemy.exc import IntegrityError
from householdRoutes import household_api

# API_BASE_URL = "URL"
CURR_USER_KEY = "curr_user"

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

# Remove SECRET_KEY for Production
app.config['SECRET_KEY'] = "SuperSecret"

app.register_blueprint(household_api, url_prefix='/household')

############################## INDEX ROUTE ##############################


@app.route('/')

def home():
    """Show home page."""

    return render_template('index.html')

############################## USER ROUTES ##############################

@app.before_request
def add_user_to_g():
    """If we are logged in, add curr_user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None

def do_login(user):
    """Log a user in."""

    session[CURR_USER_KEY] = user.id

def do_logout():
    """Log a user out."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]

@app.route("/register", methods=["GET", "POST"])
def register():
    """Produce register form and handle form submission."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]
    form = RegisterForm()

    if form.validate_on_submit():
        try:
            name = form.username.data,
            password = form.password.data

            user = User.register(name, password)
            db.session.add(user)
            db.session.commit()

        except IntegrityError as e:
            flash("Username already taken", 'danger')
            return render_template('register.html', form=form)

        do_login(user)
        session["user_id"] = user.id

        flash("You are now registered!", "success")
        return redirect("/")

    else:
        return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Produce login form and handle form submission."""

    form = LoginForm()

    if form.validate_on_submit():
        name = form.username.data
        password = form.password.data

        user = User.authenticate(name, password)

        if user:
            do_login(user)
            flash(f"Welcome, {user.username}!", "success")

            # Keep User Logged In
            session["user_id"] = user.id

            return redirect("/")

        else:
            form.username.errors = ["Bad name/password"]

    return render_template("login.html", form=form)


@app.route('/logout')
def logout():
    """Handle user logout."""

    if not g.user:
        flash("You Are Not Logged In.", "danger")
        return redirect("/")

    do_logout()
    flash('You have been logged out.', 'success')
    return redirect("/login")