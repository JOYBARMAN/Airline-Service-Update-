from django.shortcuts import render
from Main.models import Flight,Book_flight,Airlines,Flight_Book
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import AirlinesForm
from django.urls import reverse_lazy

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


class CreateAirlinesView(CreateView):
    model = Airlines
    form_class = AirlinesForm
    template_name = "airlines.html"
    success_url = reverse_lazy("airlinesList")

class AirlinesView(ListView):
    model = Airlines
    template_name = 'airlinelist.html'
    ordering = ['date']


def searchAirlines(request):
    if request.method == "POST":
        source = request.POST['ffrom']
        destination =request.POST['fto']
        flight_type =request.POST['fflight']
        airline = Airlines.objects.filter(flight_type__contains=flight_type,source__contains=source,destination__contains=destination)

        return render(request,'searchAirlines.html',{'airline':airline})
    else:
        return render(request,'searchAirlines.html',{})


def airline_detail(request,pk):
    airline = Airlines.objects.get(id=pk)
    return render(request, "airlinesDetail.html", {'airline':airline})


class UserBookFlight(ListView):
    model = Flight_Book
    template_name = 'userflight.html'
    ordering = ['created_at']