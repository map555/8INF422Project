import logging
from flask_sqlalchemy import SQLAlchemy
import datetime

from sqlalchemy.orm import relationship, backref

from projectApp.views import app

db=SQLAlchemy(app=app)

class Car(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    maker=db.Column(db.String(25),nullable=False)
    model=db.Column(db.String(25),nullable=False)
    trim=db.Column(db.String(50),nullable=False)
    mileage=db.Column(db.Integer(), db.CheckConstraint('mileage>=0'),nullable=False)
    year=db.Column(db.Integer(),db.CheckConstraint('1950<=year<='+str(datetime.datetime.today().year+1)),nullable=False)
    weight=db.Column(db.Integer(),db.CheckConstraint('weight>0'),nullable=False)
    condition=db.Column(db.Integer(),db.CheckConstraint('1<=condition<=10'),nullable=False)
    color=db.Column(db.String(25),nullable=False)
    price=db.Column(db.Integer(),db.CheckConstraint('price>0'),nullable=False)
    sold=db.Column(db.Boolean(),default=False,nullable=False)

    def __init__(self,maker,model,trim,mileage,year,
                 weight,condition,color,price,sold):
        self.maker=maker
        self.model=model
        self.trim=trim
        self.mileage=mileage
        self.year=year
        self.weight=weight
        self.condition=condition
        self.color=color
        self.price=price
        self.sold=sold

class Bill( db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    clientName=db.Column(db.String(50),nullable=False)
    carId=db.Column(db.Integer(),db.ForeignKey('car.id'))
    car=relationship("Car",backref=backref("car",uselist=False))

    def __init__(self,clientName,carId):
        self.clientName=clientName
        self.carId=carId



db.create_all()
"""
db.session.add(Car("Volkswagen","Golf","GTI",2500,2016,2972,10,"Red",22500,False))

db.session.add(Car("Mazda","Miata","Base",1011,1996,1095,10,"Yellow",10000,False))
db.session.add(Car("Hyundai","Genesis","Premium",65000,2011,3362,7,"Black",8000,False))
db.session.add(Car(maker="Hyundai",model="Genesis",trim="Premium",
                       mileage=65000,year=2011,weight=3362,
                       condition=7,color="Black",price=8000,
                       sold=False))
"""
#db.session.commit()

#logging.warning("Database initialized with a 2016 Golf GTI, a 1996 Miata and a 2011 Genesis Premium")