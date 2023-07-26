from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from contactenquiry.models import contactEnquiry
from emailenquiry.models import emailEnquiry
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')


def admission(request):
    return render(request,'kcc-admission.html')

def courses(request):
    return render(request,'kcc-courses.html')

def engineer(request):
    return render(request,'kcc-engineer.html')

def management(request):
    return render(request,'kcc-management.html')

def medical(request):
    return render(request,'kcc-medical.html')

def pg(request):
    return render(request,'kcc-pg.html')

def scholarship(request):
    return render(request,'kcc-scholarship.html')

def university(request):
    return render(request,'kcc-university.html')

def contact(request):
    return render(request,'kcc-contact.html')

def saveEnquiry(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phonenumber=request.POST.get('phonenumber')
        message=request.POST.get('message')
        saveData=contactEnquiry(name=name,email=email,phone_number=phonenumber,message=message)
        saveData.save()
        messages.success(request, " Thanks For Contacting US! We Will Get Back To You!")
        return render(request,'kcc-contact.html')
    
def saveemailEnquiry(request):
    if request.method=="POST":
        email=request.POST.get('email')
        print(email)

        eData=emailEnquiry(email_id=email)
        print(eData)
        eData.save()
        messages.success(request, " Thanks For Subscribing! We Will Get Back To You!")
        return render(request,'index.html')

