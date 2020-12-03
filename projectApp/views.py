import json
import random
import string

from flask import Flask,redirect, render_template, request, flash
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object('config')
csrf=CSRFProtect()
csrf.init_app(app)
from projectApp.models import Car, Bill
from projectApp.models import db
@app.route('/')
def home():

    return render_template('Home.html')

@app.route('/bill/billbyid')
def BillByIDView():
    return render_template('SelectBillByID.html')

@app.route('/ajax/get_bill_info_by_id', methods=['GET'])
def BillByIDRequest():
    car_info = {
                'billID': "NULL",
                'buyerName': "NULL",
                'maker': "NULL",
                'model': "NULL",
                'cartrim': "NULL",
                'mileage': "NULL",
                'caryear': "NULL",
                'carweight': "NULL",
                'condition': "NULL",
                'carcolor': "NULL",
                'price': "NULL"
                }
    if request.method=='GET':
        billID=request.values.get("bill_id")
        print(billID)

        requestBill=Bill.query.filter_by(id=billID).first()
        print(requestBill.clientName)

        requestCar = Car.query.filter_by(id=requestBill.carId).first()


        if requestBill!=None:
            bill_info={
                    'billID': billID,
                    'buyerName': requestBill.clientName,
                    'maker':requestCar.maker,
                    'model':requestCar.model,
                    'cartrim':requestCar.trim,
                    'mileage':requestCar.mileage,
                    'caryear':requestCar.year,
                    'carweight':requestCar.weight,
                    'condition':requestCar.condition,
                    'carcolor':requestCar.color,
                    'price':requestCar.price
                    }


        bill_info = {'bill_info': bill_info}

        return bill_info

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

@app.route('/bill/create', methods=['GET', 'POST'])
def CreateBill():
    if request.method == 'POST':
        billForm = request.form

        newBill = Bill(billForm['buyerName'], billForm['carId'])
        db.session.add(newBill)
        soldCar = Car.query.filter_by(id=newBill.carId).first()
        soldCar.sold = True
        db.session.commit()
        flash('Bill added')
        return ('', 204)
    else :
        return render_template('CreateBill.html')


#Bills by client name view
@app.route('/bill/billsbyclient', methods=['GET'])
def BillsByClientView():
    return render_template('BillsByClient.html')

#Bills by client name request
@app.route('/ajax/get_bills_by_client', methods=['GET'])
def BillsByClientRequest():
    bills=[]
    bill_info = None
    if request.method == 'GET':
        requestBills = Bill.query.filter_by(clientName=request.values.get("bill_client")).all()

        if requestBills:
            for x in range(len(requestBills)):
                requestCar = Car.query.filter_by(id=requestBills[x].carId).first()
                bills.append({
                    'billID': requestBills[x].id,
                    'buyerName': requestBills[x].clientName,
                    'maker':requestCar.maker,
                    'model':requestCar.model,
                    'cartrim':requestCar.trim,
                    'mileage':requestCar.mileage,
                    'caryear':requestCar.year,
                    'carweight':requestCar.weight,
                    'condition':requestCar.condition,
                    'carcolor':requestCar.color,
                    'price':requestCar.price
                    })
        else:
            bills.append({
                'billID': "NULL",
                'buyerName': "NULL",
                'maker': "NULL",
                'model': "NULL",
                'cartrim': "NULL",
                'mileage': "NULL",
                'caryear': "NULL",
                'carweight': "NULL",
                'condition': "NULL",
                'carcolor': "NULL",
                'price': "NULL"
                })

        bill_info = {'bill_info':bills}
        return bill_info

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

        if requestCars:
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




