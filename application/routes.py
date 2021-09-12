from Project1_gameshop.application.forms import AddStaff, AddStore
from application import app, db
from application.forms import AddGame,AddStore, AddStaff, UpdateGame, SelectGame
from application.models import Games, Stores, Staff
from flask import render_template, redirect, url_for, request

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/add-game', methods=['GET', 'POST'])
def add_game():
    form = AddGame()
    if request.method == 'POST':
        name = form.G_name.data
        Game = Games(G_name = name)
        db.session.add(Game)
        db.session.commit()
        return redirect(url_for('add_G'))
    return render_template('Add_game.html', form=form)

@app.route('/add-store', methods=['GET', 'POST'])
def add_store():
    form = AddStore()
    if request.method == 'POST':
        name = form.SE_name.data
        Store = Stores(SE_name = name)
        db.session.add(Store)
        db.session.commit()
        return redirect(url_for('add_SE'))
    return render_template('Add_store.html', form=form)

@app.route('/add-staff', methods=['GET', 'POST'])
def add_staff():
    form = AddStaff()
    if request.method == 'POST':
        name = form.SF_name.data
        Staff_ = Staff(SF_name = name)
        db.session.add(Staff_)
        db.session.commit()
        return redirect(url_for('add_SF'))
    return render_template('Add_staff.html', form=form)
