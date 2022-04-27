#views.py is the code for viewing the different pages and links to the login page
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Post, User
from . import db
# import os

views = Blueprint("views", __name__)
#routes for different pages
@views.route("/")
@views.route("/home")
#home page
def home():
    return render_template("home.html", user=current_user)

@views.route("/questions")
#questions
def questions():
    return render_template("questions.html", user=current_user)
#level1 workouts page
@views.route("/level1")

def level1():
    return render_template("level1.html", user=current_user)
#level2 workouts page
@views.route("/level2")

def level2():
    return render_template("level2.html", user=current_user)
#level3 workouts page
@views.route("/level3")

def level3():
    return render_template("level3.html", user=current_user)


#requires login in order to view posts made, when logged in you can view all of your posts
@views.route("/view_posts", methods = ["GET"])
@login_required
def view_posts():
    posts = Post.query.all()
    return render_template("view_posts.html", user=current_user, posts=posts)

# get post is how we input data into the back end
@views.route("/create-post", methods=['GET', 'POST'])
#takes the input the user inputted from the form, only when logged in
@login_required
def create_post():
    if request.method == "POST":
        #gets user inputs and stores in variable
        text = request.form.get('text')
        text1 = request.form.get('text1')
        text2 = request.form.get('text2')
        text3 = request.form.get('text3')
        text4 = request.form.get('text4')
        text5  = request.form.get('text5')
        #get user input for amount of water that was drank and outputs whether user should drink more or less water based on input
        water=""
        if (text.isnumeric()):
            water = int(text)
            if water < 15:
                text = "You need to drink more water!"
                water=text
            elif water >= 15:
                text = "You drank enough water today, good job!"
        #get user input for intensity of workout and outputs based on how intense it was
        intensity=""
        if (text1.isnumeric()):
            intensity = int(text1)
            if intensity == 4:
                text1 = "It's time to do some workout!"
            elif 2 < intensity < 4:
                text1 = "Way to get an intense workout!"
            elif intensity >= 2 and intensity <=3:
                text1 = "Good job getting a workout in today!"
            elif intensity >= 4:
                text1 = "Way to get some rest today"
        #takes user input for soreness and returns a statement based on that
        sore = ""
        if (text2.isnumeric()):
            sore = int(text2)
            if sore < 7:
                text2 = "It's good you're not that sore today!"
                #sore = text2
            elif sore >= 7:
                text2 = "Your body seems pretty sore!"
        #get input for how long user worked out for and returns if they should rest or work on based on hours, intensity, and soreness
        hours = ""
        if (text3.isnumeric()):
            hours = int(text3)
            if hours > 6:
                text3 = "You really need to rest today so you don't put your body in a bad place"
                #hours = text3
            if not (text and text1 and text2 and text3 and text4 and text5):
                flash('Enter the details', category='error')
            elif hours<=6:
                if (int(intensity)>2 and int(sore)<7):
                    text3 = "You are good to get a good workout in!"
                if (int(intensity)<=2 and int(sore)>7):
                    text3 = "You should rest today since you're sore and got a good workout in!"
                if (int(intensity)<=2 and int(sore)<7):
                    text3 = "You are good to get a good workout in!"
                if (int(intensity)>2 and int(sore)>7):
                    text3 = "You are good to get a light workout in since you're pretty sore!"
        #takes input for how much sleep user got and returns statement based on tbat
        sleep = ""
        if (text4.isnumeric()):
            sleep = int(text4)
            if sleep >= 8:
                text4 = "You got a good amount of sleep last night."
            elif sleep < 8:
                text4 = "You should get some more sleep so your body isn't as tired."
        #checks how user is mentally and tells them to continue working on themself or gives a page they should check out if struggling mentally
        mental = ""
        if (text5.isnumeric()):
            mental = int(text5)
            if mental > 7:
                text5 = "You should check out this page: https://uhs.umich.edu/tenthings"
            elif mental <= 7:
                text5 = "Continue working on yourself!"

        if not (text and text1 and text2 and text3 and text4 and text5):
            flash('Enter the details', category='error')
        # made changes here
        elif not (water == text):
            flash('Please enter a numeric value in cups', category='error')
        elif not (intensity == text1):
            flash('Please enter a numeric value for your intensity: 1, 2, or 3', category='error')
        elif not (sore == text2):
            flash('Please enter a numeric value for how sore you are: 1-10', category='error')
        elif not (hours == text3):
            flash('Please enter a numeric value for how many hours you worked out for', category='error')
        elif not (sleep == text4):
            flash('Please enter a numeric value for how many hours of sleep you got', category='error')
        elif not (mental == text5):
            flash('Please enter a numeric value for how you are feeling mentally', category='error')

        else:
            post = Post(text=text,text1=text1,text2=text2,text3=text3,text4=text4,text5=text5,author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('The data is submitted', category='success')
            return redirect(url_for('views.view_posts'))

    return render_template('create_post.html', user=current_user)
@views.route("/delete-post/<id>")
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()
    if not post:
        flash("Post does not exist.", category='error')
    elif current_user.id == post.id:
        flash('You do not have permission to delete this post.', category='error')
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted', category='success')
    return redirect(url_for('views.view_posts'))

@views.route("/posts/<username>")
@login_required
def posts(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        flash('No user with that username exists.', category='error')
        return redirect(url_for('views.view_posts'))
    posts=Post.query.filter_by(author=user.id).all()
    return render_template("posts.html", user=current_user, posts=posts, username=username)
