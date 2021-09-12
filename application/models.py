from application import db

class Stores(db.model):
    id = db.Column(db.Integer, primary_key = True)
    Store_address = db.Column(db.string(100))
    Store_phone_number = db.Column(db.string(20))
    Staff_ID = db.Column(db.integer , db.Foreignkey('staff.id'))
    Store_stock = db.relationship('Stock', backref='store')

class Staff(db.model):
    id = db.Column(db.Integer, primary_key = True)
    Staff_name = db.Column(db.String(50))
    Staff_address = db.column(db.String(100))
    Staff_phone_number = db.column(db.string(20))
    Staff_stock = db.relationship('Stores', backref='staff')

class Games(db.model):
    id = db.Column(db.Integer, primary_key = True)
    Game_name = db.Column(db.String(50))
    Game_age_rating = db.column(db.Integer)
    Game_price = db.column(db.Decimal)
    Games_stock = db.relationship('Stock', backref='Games')

class Stock(db.model):
    id = db.Column(db.Integer, primary_key = True)
    Game_id = db.Column('Game_id', db.Integer, db.ForeignKey('Games.id'))
    Store_id = db.Column('Store_id', db.Integer, db.ForeignKey('Stores.id'))
