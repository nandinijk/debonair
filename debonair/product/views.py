from django.shortcuts import render
from .models import TravelPlace

# Create your views here.
def details(request):
    id=request.GET['id']
    pro=TravelPlace.objects.get(id=id)
    print(pro)

    return render(request,'single.html',{'p':pro})

