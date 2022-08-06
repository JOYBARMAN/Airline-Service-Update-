from django.shortcuts import (get_object_or_404,render,HttpResponseRedirect)
from Main.models import Airlines,Flight_Book
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView
from .forms import AirlinesForm,FlightBookForm
from django.urls import reverse_lazy

def index(request):
    return render(request,'index.html')

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
    # ordering = ['-id']


class EditAirlinesView(UpdateView):
    model = Airlines
    form_class = AirlinesForm
    template_name = 'edit-airlines.html'
    success_url = reverse_lazy("airlinesList")


def searchAirlines(request):
    if request.method == "POST":
        source = request.POST['ffrom']
        destination =request.POST['fto']
        flight_type =request.POST['fflight']
        flying_date = request.POST['date']
        airline = Airlines.objects.filter(flying_date__contains=flying_date,flight_type__contains=flight_type,source__contains=source,destination__contains=destination)
        # airline = Airlines.objects.filter(flying_date__contains=flying_date)

        return render(request,'searchAirlines.html',{'airline':airline})
    else:
        return render(request,'searchAirlines.html',{})


def airline_detail(request,pk):
    airline = Airlines.objects.get(id=pk)
    airline_list=Airlines.objects.all()
    return render(request, "airlinesDetail.html", {'airline':airline,'airline_list':airline_list})

def delete_airline_view (request,id):
    context ={}
    obj = get_object_or_404(Airlines, id = id)
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/airlineslist")
    return render(request, "deleteAirline.html", context)


class UserBookFlight(ListView):
    model = Flight_Book
    template_name = 'userflight.html'
    ordering = ['created_at']


def flight_cancel_view(request, id):
    context ={}
    obj = get_object_or_404(Flight_Book, id = id)
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/userflight")
    return render(request, "cancelflight.html", context)

class BookFlightView(CreateView):
    model = Flight_Book
    form_class = FlightBookForm
    template_name = "book_flight.html"
    success_url = reverse_lazy("userflight")

def book_flight(request):
    if request.method == "POST":
        user = request.user
        airline_id = request.POST.get('airlines')
        airline = Airlines.objects.get(id=airline_id)
        flightbook = Flight_Book(user=user,airlines=airline)
        flightbook.save()
        messages.success(request,'Your Flight Is Successfully Booked')
        return HttpResponseRedirect("/userflight")




