from email.policy import HTTP
from django.shortcuts import render
from django.http import HttpResponse
from product.models import TravelPlace


# Create your views here.





#def samp(request):
    
    #return render(request,'test.html',{'l':pro})

def samp(request):
    data=TravelPlace.objects.all()
    

    return render(request,'index.html',{'d':data})

def sam(request):
    
    return render(request,'login.html')

def regi(request):
    
    return render(request,'register.html')

def sub(request):
    return render(request,'test.html')