from . import db

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    numofBed = db.Column(db.Integer)
    numofBath = db.Column(db.Integer)
    location = db.Column(db.String(80))
    price = db.Column(db.Numeric(15,2))
    typeOfHouse = db.Column(db.String(80))
    description = db.Column(db.String(255))
    photoName = db.Column(db.String(80))
    
    def __init__(self,title,numofBed,numofBath,location,price,typeOfHouse,description,photoName):
        self.title = title
        self.numofBed = numofBed
        self.numofBath = numofBath
        self.location = location
        self.price = price
        self.typeOfHouse = typeOfHouse
        self.description = description
        self.photoName = photoName

    def __repr__(self):
        return '<User %r>' % (self.title)