from email.policy import HTTP
from django.shortcuts import render
from django.http import HttpResponse
from .models import product


# Create your views here.



p1=product()
p1.name="loreal"
p1.price=200
p1.dsc="best hair shampoo"

p2=product()
p2.name="tresemme"
p2.price=400
p2.dsc="have slight sulphate content"

p3=product()
p3.name="arata"
p3.price=250
p3.dsc="curly hair friendly shampoo"

p4=product()
p4.name="himalaya"
p4.price=180
p4.dsc="shampoo for dry skin"

pro=[p1,p2,p3,p4]

#def samp(request):
    
    #return render(request,'test.html',{'l':pro})

def samp(request):
    
    return render(request,'index.html')

def sam(request):
    
    return render(request,'login.html')

def regi(request):
    
    return render(request,'register.html')

def sub(request):
    return render(request,'test.html')