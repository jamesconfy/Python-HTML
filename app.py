from flask import Flask, request, render_template, url_for
from db import *

app = Flask(__name__)

@app.route('/')
def all_data():
    db = DB()
    data = db.GetAll()

    return render_template('alldata.html', data=data)

@app.route('/home')
def new_profile():
    return render_template('home.html')

@app.route('/create_profile', methods=['GET', 'POST'])
def create_profile():
    db = DB()

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    dob = request.form['dob']
    address = request.form['address']
    city = request.form['city']
    state = request.form['state']
    phone_no = request.form['phone_no']
    
    db.CreateProfile(first_name, last_name, dob, address, city, state, phone_no)
    
    data = db.GetAll()
    return render_template('alldata.html', data=data)

@app.route('/view_profile')
def view_profile():
    db = DB()
    id = request.args["id"]

    data = db.GetByID(id)

    return render_template("viewprofile.html", data=data)

@app.route('/delete_profile')
def delete_profile():
    db = DB()
    id = request.args["id"]

    db.DeleteProfileByID(id)

    data=db.GetAll()

    return render_template('alldata.html', data=data)

@app.route('/update_profile', methods=['GET', 'POST'])
def update_profile():
    db = DB()
    id = request.args["id"]

    data = db.GetByID(id)
    print(data)
    return render_template('update_profile.html', data=data)

@app.route('/update', methods=['GET', 'POST'])
def update_all():
    db = DB()
    
    id = request.args["id"]
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    dob = request.form['dob']
    address = request.form['address']
    city = request.form['city']
    state = request.form['state']
    phone_no = request.form['phone_no']
    
    db.UpdateAll(id, first_name, last_name, dob, address, city, state, phone_no)

    data = db.GetAll()
    return render_template('alldata.html', data=data)