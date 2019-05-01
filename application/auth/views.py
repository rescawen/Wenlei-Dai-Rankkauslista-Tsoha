from flask import render_template, flash, request, redirect, url_for
from flask_login import login_user, logout_user
  
from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegistrationForm

@app.route("/auth/login", methods = ["POST"])
def auth_login():
    form = LoginForm(request.form)
    
    if not form.validate():
        return render_template("index/index.html", form = form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        flash('No such username or password')
        return redirect(url_for("index"))   

    login_user(user)
    return redirect(url_for("index"))    

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))  

@app.route("/auth/new/")
def auth_new():
    return render_template("auth/createform.html", form = RegistrationForm())

@app.route("/auth/create", methods=["POST"])
def auth_create():
    form = RegistrationForm(request.form)

    if not form.validate():
        return render_template("auth/createform.html", form = form)

    newUser = User(form.name.data, form.username.data, form.password.data)
    
    db.session().add(newUser)
    db.session().commit()

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    login_user(user)
    return redirect(url_for("index"))  
