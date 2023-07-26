from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path('', views.index,name="home"),
    path('about-us/', views.about,name="about"),
    path('contact-us/', views.contact,name="contact"),
    path('kcc-admission/',views.admission,name="admission"),
    path('kcc-courses/', views.courses,name="courses"),
    path('kcc-engineering/', views.engineer,name="engineer"),
    path('kcc-management/',views.management,name="management"),
    path('kcc-medical-courses/', views.medical,name="medical"),
    path('kcc-pg/', views.pg,name="pg"),
    path('kcc-universities/',views.university,name="university"),
    path('kcc-scholarship/',views.scholarship,name="scholarship"),
    path('saveenquiry/',views.saveEnquiry,name="saveenquiry"),
    path('emailenquiry/',views.saveemailEnquiry,name="emailEnquirySave"),
]
