from django.shortcuts import render
from django.http import HttpResponse
import joblib


def safe(request):
    return render(request,'findsafe.html')
def result(request):

    model_b = joblib.load("Airline_fatalities_predictor.pkl")

    lis = []

    lis.append(request.GET['fatal_accident'])

    ans = model_b.predict([lis])[0].round(0)




    return render(request,'result.html',{'ans':ans})
