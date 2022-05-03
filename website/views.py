#contains all the views and links to the other html files created
#imports necessary
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Post, User
from . import db

views = Blueprint("views", __name__)
#links to home page
@views.route("/")
@views.route("/home")
#links to home html file/page
def home():
    return render_template("home.html", user=current_user)

@views.route("/questions")
#for questions tab
def questions():
    return render_template("questions.html", user=current_user)

@views.route("/level1")
#for level1 tab
def level1():
    return render_template("level1.html", user=current_user)
#for level2 tab
@views.route("/level2")

def level2():
    return render_template("level2.html", user=current_user)
#for level3 tab
@views.route("/level3")

def level3():
    return render_template("level3.html", user=current_user)


#to view the users posts, links to view posts html
@views.route("/view_posts/", methods = ["GET"])
@login_required
def view_posts():
    posts = Post.query.all()
    return render_template("view_posts.html", user=current_user, posts=posts)

# get post is how we input data into the back end
@views.route("/create-post", methods=['GET', 'POST'])
#login needed to create a post
@login_required
#logic for user input to give them back feedback
def create_post():
    if request.method == "POST":
        #store user input in variables
        text = request.form.get('text')
        text1 = request.form.get('text1')
        text2 = request.form.get('text2')
        text3 = request.form.get('text3')
        text4 = request.form.get('text4')
        text5  = request.form.get('text5')
        #logic for water, outputs whether user should drink more or less water
        #checks to make sure user input is a number and within range when required
        water=""
        if (text.isnumeric()):
            water = int(text)
            if water < 15:
                text = "You need to drink more water!"
                water=text
            elif water >= 15:
                text = "You drank enough water today, good job!"
                water = text
        #logic for intensity telling the user good feedback
        intensity=0
        report1 = ""
        if (text1.isnumeric() and (text1 == "1" or text1 == "2" or text1 == "3" or text1 == "4")):
            intensity = int(text1)
            if intensity<2:
                text1 = "Way to get an intense workout in!"
            elif intensity >= 2 or intensity <=3:
                text1 = "Good job getting a workout in today!"
            elif intensity >= 4:
                text1 = "Way to get some rest today"
            report1 = text1
        #gives user feedback depending on their soreness level
        sore = ""
        report2 = ""
        if (text2.isnumeric() and (1<=int(text2)<=10)):
            sore = int(text2)
            if sore < 7:
                text2 = "It's good you're not that sore today!"
            elif sore >= 7:
                text2 = "Your body seems pretty sore!"
            report2 = text2
        #tells user whether to rest or not depending on hours, soreness, and intensity
        hours = ""
        report3 = ""
        if text3.replace(".", "").isdigit():
            hours = float(text3)
            if hours > 6:
                text3 = "You really need to rest today so you don't put your body in a bad place"
                # hours = text3
            if not (sore and intensity):
                flash('Enter the details', category='error')
            elif not (text and text1 and text2 and text3 and text4 and text5):
                flash('Enter the details', category='error')
            elif hours <= 6:
                if (int(intensity) > 2 and int(sore) < 7):
                    text3 = "You are good to get a good workout in!"
                if (int(intensity) <= 2 and int(sore) > 7):
                    text3 = "You should rest today since you're sore and got a good workout in!"
                if (int(intensity) <= 2 and int(sore) < 7):
                    text3 = "You are good to get a good workout in!"
                if (int(intensity) > 2 and int(sore) > 7):
                    text3 = "You are good to get a light workout in since you're pretty sore!"
            report3 = text3
        elif (text3.isnumeric()):
            hours = float(text3)
            if hours > 6:
                text3 = "You really need to rest today so you don't put your body in a bad place"
                #hours = text3
            if not (sore and intensity):
                flash('Enter the details', category='error')
            elif not (text and text1 and text2 and text3 and text4 and text5):
                flash('Enter the details', category='error')
            elif hours <=6:
                if (int(intensity)>2 and int(sore)<7):
                    text3 = "You are good to get a good workout in!"
                if (int(intensity)<=2 and int(sore)>7):
                    text3 = "You should rest today since you're sore and got a good workout in!"
                if (int(intensity)<=2 and int(sore)<7):
                    text3 = "You are good to get a good workout in!"
                if (int(intensity)>2 and int(sore)>7):
                    text3 = "You are good to get a light workout in since you're pretty sore!"
            report3 = text3
        #takes user input and reports if they got enough sleep or not
        sleep = ""
        if text4.replace(".", "").isdigit():
            sleep = float(text4)
            if sleep >= 8:
                text4 = "You got a good amount of sleep last night."
            elif sleep < 8:
                text4 = "You should get some more sleep so your body isn't as tired."
            sleep = text4
        if (text4.isnumeric()):
            sleep = float(text4)
            if sleep >= 8:
                text4 = "You got a good amount of sleep last night."
            elif sleep < 8:
                text4 = "You should get some more sleep so your body isn't as tired."
            sleep = text4
        #checks how user is mentally and gives a website to check out if they are not mentally well
        mental = ""
        if (text5.isnumeric() and (1<= int(text5) <= 10)):
            mental = int(text5)
            if mental>7:
                text5 = "You should check out this page: https://uhs.umich.edu/tenthings"
            elif mental<=7:
                text5 = "Continue working on yourself!"
            mental = text5
        #error flashes when not all questions are answered and if they don't enter numeric value
        if not (text and text1 and text2 and text3 and text4 and text5):
            flash('Enter the details', category='error')

        elif not (water == text):
            flash('Please enter a numeric whole value in cups', category='error')
        elif  (report1 != text1):
            flash('Please enter a numeric value for your intensity: 1, 2, 3, or 4', category='error')
        elif not (report2 == text2):
            flash('Please enter a numeric value for how sore you are: 1-10', category='error')
        elif not (report3 == text3):
            flash('Please enter a numeric value for how many hours you worked out for', category='error')
        elif not (sleep == text4):
            flash('Please enter a numeric value for how many hours of sleep you got', category='error')
        elif not (mental == text5):
            flash('Please enter a numeric value for how you are feeling mentally', category='error')
        #if no error occurred, then data entered is good and report to user that their data was submitted
        #redirects user to view_posts where they see all of their posts
        else:
            post = Post(text=text,text1=text1,text2=text2,text3=text3,text4=text4,text5=text5,author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('The data is submitted', category='success')
            return redirect(url_for('views.view_posts'))
    return render_template('create_post.html', user=current_user)
@views.route("/delete-post/<id>")
@login_required
#allows user to delete post only if they are the one who created the post and flashes if they deleted it or if they don't have permission
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
#filters users posts so they can only see their on post
def posts(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        flash('No user with that username exists.', category='error')
        return redirect(url_for('views.view_posts'))
    posts=Post.query.filter_by(author=user.id).all()
    return render_template("posts.html", user=current_user, posts=posts, username=username)