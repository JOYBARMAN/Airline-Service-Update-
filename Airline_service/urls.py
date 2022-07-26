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
from django.contrib import admin
from django.urls import path,include
from Feedback import urls
from Feedback.views import contact
admin.site.site_header = "Airline service admin "
admin.site.site_title = "Airline service Admin Portal"
admin.site.index_title = "Welcome to Airline service Portal"
#from Main import views as mg
from Main.views import index,available,davailable,home
from Authentication.views import signup,login,logout
from Find_safe.views import safe,result
from Price_prediction.views import price,result1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ind/',index,name="index"),
    path('',home,name="home"),
    path('ava/',available),
    path('dava/',davailable),
    path('reg/',signup,name="signup"),
    path('login/',login, name="login"),
    path('logout/',logout,name="logout"),
    path('contact/',contact,name="contact"),
    path('sf/',safe, name="safe"),
    path('result/',result, name="result"),
    path('price/', price ,name="price"),
    path('result1/', result1, name="result1"),
]
