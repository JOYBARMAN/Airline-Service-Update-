from django.shortcuts import render
from Main.models import Flight,Book_flight
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse


def index(request):
    if request.method == "POST":
        fflight = request.POST.get('fflight')
        ffrom = request.POST.get('ffrom')
        fto = request.POST.get('fto')
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        adult = request.POST.get('adult')
        child = request.POST.get('child')
        fclass = request.POST.get('fclass')
        flight = Flight(fflight=fflight, ffrom=ffrom, fto=fto, date1=date1, date2=date2, adult=adult, child=child, fclass=fclass)
        flight.save()
        if request.POST['fflight'] == "Domestic" :
            return redirect(davailable)
        else:
            return redirect(available)
    else :
        return render(request,'index.html')



def available(request):
    if request.method == "POST":
        sflight = request.POST.get('sflight')
        passport_num = request.POST.get('passport_num')
        flight2 = Book_flight(sflight=sflight, passport_num=passport_num)
        messages.success(request, 'Your Flight is Successfully Booked')
        flight2.save()
        return redirect(index)
    else:
        return render(request,'available.html')

def davailable(request):
    if request.method == "POST":
        sflight = request.POST.get('sflight')
        passport_num = request.POST.get('passport_num')
        flight2 = Book_flight(sflight=sflight, passport_num=passport_num)
        flight2.save()
        messages.success(request, 'Your Flight is Successfully Booked')
        return redirect(index)
    else:
        return render(request,'davailable.html')


def home(request):
    return render(request,'home.html')
