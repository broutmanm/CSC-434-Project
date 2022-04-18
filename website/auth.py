from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    render_template("login.html")


@auth.route("/sign-up")
def sign_up():
    return render_template("signup.html")


@auth.route("/logout")
def logout():
    return render_template("home.html", name="Mohamad")
