from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from pymongo import MongoClient
from . import registerFace as rf
from . import loadFace as lf

from bson.objectid import ObjectId
from bson import json_util

import json

#db connection
client = MongoClient('mongodb://localhost:27017/')

db = client["medical"]
col = db["patient_history"]
data = ''

# Create your views here.
def home(request):
    return render(request, 'home.html')

#to show the register html page.
def register(request):
    return render(request, 'register.html')

#to show that registration process is complete
def registerComplete(request):
    return render(request, 'registerComplete.html')

#register Image python file.
def getFace(request):
    if(request.method == 'POST'):
        userId = request.POST.get("userId")
        rf.startCamera(userId)
    return render(request, 'registerComplete.html')

#login using image python file.
def loadFace(request):
    userId = lf.loadCamera()
    data = [doc for doc in col.find({"_id" : ObjectId(userId)})]
    # rowData = json.dumps(data)
    # [data for data in col.find({"_id": ObjectId(userId)})]
    # json_docs = [json.dumps(doc, default=json_util.default) for doc in data]
    # image, Fname, Lname, gender, email, birthday = json_docs
    # data = [i for i in col.find({"_id": ObjectId(userId)})]
    # firstName = data[0]["firstName"]
    # lastName = data[0]["lastName"]
    # gender = data[0]["gender"]
    #         "email": email,
    #         "password":  password,
    #         "birthday": birthday
    _id , firstName, lastName, gender, email, password, birthday = data[0].values()
    return render(request, 'filledForm.html', {"data": data, "photo": _id, "firstName": firstName, "lastName": lastName, "gender": gender, "email": email, "password":  password, "birthday": birthday})

#to show the filled form.
def filledform(request):
    return render(request, 'filledform.html')

#to register the  data provided  by patient.
def registerUser(request):
    if(request.method == 'POST'):
        firstname = request.POST.get('Fname')
        lastname = request.POST.get('Lname')
        gender = request.POST.get('Gender')
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        birthday = request.POST.get('birthday')

        patient = { 
            "firstName": firstname, 
            "lastName": lastname, 
            "gender": gender,
            "email": email,
            "password":  password,
            "birthday": birthday
        }

        userId= col.insert(patient)

        return render(request, "registerImage.html", {"userId": userId})