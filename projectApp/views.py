import json
import random
import string

from flask import Flask,redirect, render_template, request, flash
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object('config')
csrf=CSRFProtect()
csrf.init_app(app)
from projectApp.models import Car
from projectApp.models import db
@app.route('/')
def home():

    return render_template('Home.html')


#Car by ID page
@app.route('/car/carbyid')
def CarByIDView():
    return render_template('CarByID.html')

#Car by ID request
@app.route('/ajax/get_car_info_by_id',methods=['GET'])
def CarByIDBDRequest():
    car_info = {'maker': "NULL",
               'model': "NULL",
               'cartrim': "NULL",
               'mileage': "NULL",
               'caryear': "NULL",
               'carweight': "NULL",
               'condition': "NULL",
               'carcolor': "NULL",
               'price': "NULL"}

    if request.method=='GET':
        carID=request.values.get("car_id")
        print(carID)

        requestCar=Car.query.filter_by(id=carID).first()


        if requestCar!=None and requestCar.sold==False:
            car_info={'maker':requestCar.maker,
                    'model':requestCar.model,
                    'cartrim':requestCar.trim,
                    'mileage':requestCar.mileage,
                    'caryear':requestCar.year,
                    'carweight':requestCar.weight,
                    'condition':requestCar.condition,
                    'carcolor':requestCar.color,
                    'price':requestCar.price}


        car_info = {'car_info': car_info}

        return car_info

        #response=app.response_class(json.dump(car_info),status=400,mimetype='application/json')

    #return response


#Create car view and request
@app.route('/car/create',methods=['GET','POST'])
def CreateCar():

    if request.method=='POST':
        carForm = request.form

        newCar = Car(carForm['car_maker'], carForm['car_model']
                     , carForm['car_trim'], int(carForm['car_mileage']),
                     int(carForm['car_year']), int(carForm['car_weight']),
                     int(carForm['car_condition']), carForm['car_color'],
                     int(carForm['car_price']), False)
        db.session.add(newCar)
        db.session.commit()
        flash('Car added')
        return ('',204)
    else:
        return render_template('CreateCar.html')


#Cars by maker view
@app.route('/car/carsbymaker',methods=['GET'])
def CarsByMakerView():
    return render_template('CarsByMaker.html')

#Cars by maker request
@app.route('/ajax/get_cars_by_maker',methods=['GET'])
def CarsByMakerRequest():
    cars=[]
    car_info=None
    if request.method=='GET':
        requestCars=Car.query.filter_by(maker=request.values.get("car_maker"),sold=False).all()

        if requestCars!=None:
            for x in range(len(requestCars)):
                cars.append({'maker': requestCars[x].maker,
               'model': requestCars[x].model,
               'cartrim': requestCars[x].trim,
               'mileage': requestCars[x].mileage,
               'caryear': requestCars[x].year,
               'carweight': requestCars[x].weight,
               'condition': requestCars[x].condition,
               'carcolor': requestCars[x].color,
               'price': requestCars[x].price})



        else:
            cars.append({'maker': "NULL",
               'model': "NULL",
               'cartrim': "NULL",
               'mileage': "NULL",
               'caryear': "NULL",
               'carweight': "NULL",
               'condition': "NULL",
               'carcolor': "NULL",
               'price': "NULL"})


        car_info={'car_info':cars}

        return car_info




