from flask import Blueprint, g, render_template, flash, redirect
from models import db, connect_db, UserHousehold

household_api = Blueprint('home_api', __name__)

@household_api.route("/", methods=["GET"])
def home_list():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")
    
    household = UserHousehold.query.filter(UserHousehold.userID == g.user.id).all()

    return render_template('homeList.html', household=household)

