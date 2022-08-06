"""Airline_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from Feedback import urls
from Feedback.views import contact
admin.site.site_header = "Airline service admin "
admin.site.site_title = "Airline service Admin Portal"
admin.site.index_title = "Welcome to Airline service Portal"
#from Main import views as mg
from Main.views import index,home,CreateAirlinesView,AirlinesView,searchAirlines,airline_detail,UserBookFlight,flight_cancel_view,book_flight,EditAirlinesView,delete_airline_view
from Authentication.views import signup,login,logout
from Find_safe.views import safe,result
from Price_prediction.views import price,result1
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ind/',index,name="index"),
    path('',home,name="home"),
    path('reg/',signup,name="signup"),
    path('login/',login, name="login"),
    path('logout/',logout,name="logout"),
    path('contact/',contact,name="contact"),
    path('sf/',safe, name="safe"),
    path('result/',result, name="result"),
    path('price/', price ,name="price"),
    path('result1/', result1, name="result1"),
    path('airlines/',CreateAirlinesView.as_view(),name="airlines"),
    path('airlineslist',AirlinesView.as_view(),name="airlinesList"),
    path('airlinedetail/<int:pk>',airline_detail,name="airline_detail"),
    path('airline/<id>/delete', delete_airline_view, name="delete-airline"),
    path('airline/<int:pk>/edit',EditAirlinesView.as_view(),name="airline_edit"),
    path('searchairline',searchAirlines,name="searchairline"),
    path('userflight',UserBookFlight.as_view(),name="userflight"),
    path('userflight/<id>/cancel', flight_cancel_view, name="cancel-flight"),
    path('bookflight',book_flight,name="bookflight")
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)