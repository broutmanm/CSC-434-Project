from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Post
from . import db

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")

def home():
    return render_template("home.html", user=current_user)

@views.route("/view_posts")
@login_required
def view_posts():
    posts = Post.query.all()
    return render_template("view_posts.html", user=current_user, posts=posts)

@views.route("/create-post", methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == "POST":
        text = request.form.get('text')
        text1 = request.form.get('text1')
        text2 = request.form.get('text2')
        text3 = request.form.get('text3')
        text4 = request.form.get('text4')
        text5  = request.form.get('text5')

        water = int(text)
        if water<=15:
            text="You need to drink more water!"
        else:
            text="You drank enough water today, good job!"
        intensity = int(text1)


        if not (text and text1 and text2 and text3 and text4 and text5):
            flash('Enter the details', category='error')
        else:
            post = Post(text=text,text1=text1,text2=text2,text3=text3,text4=text4,text5=text5,author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('The data is submitted', category='success')
            return redirect(url_for('views.view_posts'))
    return render_template('create_post.html', user=current_user)