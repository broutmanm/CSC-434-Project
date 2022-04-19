from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
db_locale = 'students.db'

@app.route('/')
@app.route('/home')
def home_page():
    student_data = query_contact_details()
    return render_template('home.html', student_data=student_data)

@app.route('/add')
def add_student():
    return 'Here is where we add students'

def query_contact_details():
    connie = sqlite3.connect(db_locale)
    c = connie.cursor()
    c.execute("""
    SELECT * FROM contact
    """)
    student_data = c.fetchall()
    return student_data

@app.route('/add', methods = ["GET", "POST"])
def check_input():
    if request.method == "POST":
        form = request.form
        question1 = int(form("question1"))
        question1 = int(form("question1"))



if __name__ == '__main__':
    app.run()
