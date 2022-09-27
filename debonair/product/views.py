from django.shortcuts import render,redirect
from .models import TravelPlace,comment

# Create your views here.
def details(request):
    id=request.GET['id']
    pro=TravelPlace.objects.get(id=id)
    cmt=comment.objects.filter(place_id=id)
    print(pro)

    return render(request,'single.html',{'p':pro,'cmt':cmt})

def commenting(request):
    msg=request.GET['msg']
    pro_id=request.GET['pro_id']
    user=request.GET['user']
    cmt=comment.objects.create(cmt=msg,name=user,place_id=pro_id)
    cmt.save();
    return redirect('/')
