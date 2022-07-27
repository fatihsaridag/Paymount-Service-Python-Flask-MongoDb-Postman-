from email.policy import default
import json
from lib2to3.pytree import convert
from traceback import print_tb
from turtle import pen
from flask import Flask, jsonify,render_template,flash,redirect,url_for
from flask import request
from wtforms import Form,StringField,TextAreaField,PasswordField,validators,DateField,BooleanField,IntegerField
import pymongo

 
 

 
 
app = Flask(__name__)   

 

@app.route('/register', methods= ["GET", "POST"])
def register() : 
    request_data = request.get_json()
    ad = request_data['FirstName']
    soyad = request_data['LastName']
    cinsiyet = request_data['Gender']
    odeme_servisi = request_data['purchased_service']
    odeme_miktari = request_data['amount_payment']
    
    myclient = pymongo.MongoClient('mongodb://localhost:27017')
    mydb = myclient['mydatabase']
    mycol = mydb['users']
    mydict =  {'FirstName' : ad , 'LastName' : soyad , 'Gender' : cinsiyet , 'purchased_service' : odeme_servisi , 'amount_payment' : odeme_miktari}
    mycol.insert_one(mydict)
    return  "Root working register"


@app.route('/purchase', methods = ["GET", "POST"])
def purchase() : 
    request_data = request.get_json() 
    ad = request_data['FirstName']
    soyad = request_data['LastName']
    odeme_miktari = request_data['amount_payment']


    if odeme_miktari == 100 :
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["users"]
        myquery = { "FirstName": ad , "LastName" : soyad } 
        mydoc = mycol.find(myquery)
        newvalues = { "$set": { "purchased_service": True } }
        mycol.update_one(myquery, newvalues)
        return "Güncellendi"
    else : 
        return "Güncellenmedi"



@app.route('/paidservice', methods = ["GET", "POST"])
def paidservice() : 
        request_data = request.get_json() 
        ad = request_data['FirstName']
        soyad = request_data['LastName']
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["users"]
        myquery = { "FirstName": ad , "LastName" : soyad } 
        myquery2 = {'purchased_service': True}        
        if myquery2 : 
               myclient = pymongo.MongoClient("mongodb://localhost:27017/")
               mydb = myclient["mydatabase"]
               mycol = mydb["users"]
               myquery = { "FirstName": ad , "LastName" : soyad } 
               mydoc = mycol.find(myquery)
               newvalues = { "$set": { "purchased_service": False } }
               mycol.update_one(myquery, newvalues)
               return "Hoşgeldiniz servisler tekrar kullanıma açıktır."
        else : 
                 return "Bu servisi kullanmak için satın almalısınız"



         
        

if __name__ == "__main__":
	app.run(debug=True)