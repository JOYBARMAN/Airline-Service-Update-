from django.shortcuts import render
from Feedback.models import Contact
from django.contrib import messages
from datetime import datetime
from django.http import HttpResponse

def contact(request):
    if request.method == "POST":
        user=request.user
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(user=user,name=name, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request,'Your Feedback information have been send successfully ')
    return render(request,'contact.html')