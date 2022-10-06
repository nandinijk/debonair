from email.policy import HTTP
from django.shortcuts import render,redirect
from django.http import HttpResponse
from product.models import TravelPlace
from django.contrib.auth.models import User,auth


# Create your views here.





#def samp(request):
    
    #return render(request,'test.html',{'l':pro})

def samp(request):
    if request.method=="POST":
        val=request.POST['searchbox']
        data=TravelPlace.objects.filter(name__istartswith=val)
    else:
        data=TravelPlace.objects.all()
   
    

    return render(request,'index.html',{'d':data})




def sam(request):
    
    return render(request,'login.html')

def regi(request):
    
    if request.method=='POST':
        uname=request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['Lname']
        email=request.POST['email']
        p1name=request.POST['Pname1']
        p2name=request.POST['pname2']
        ucheck=User.objects.filter(username=uname)
        echeck=User.objects.filter(email=email)
        if ucheck:
            msg="username already exists"
            return render(request,"register.html",{'msg':msg})

        elif echeck:
            msg="email already exists"
            return render(request,"register.html",{'msg':msg})
        
        elif p1name!=p2name:
            msg="password incorrect"
            return render(request,"register.html",{'msg':msg})
        else :
            user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,password=p1name,email=email)
            user.save();
            return redirect("/")
    else:
        return render(request,'register.html')

def sub(request):
    uname=request.POST['uname']
    pname=request.POST['pword']
    user=auth.authenticate(username=uname,password=pname)
    if user is not None:
        auth.login(request,user)
        return redirect("/")
    else:
        return render(request,'test.html')
    return render(request,'test.html')
