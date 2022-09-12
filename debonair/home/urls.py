from django.urls import path
from . import views 

urlpatterns = [
    
    path('test/',views.samp),
    path('login/',views.sam),
    path('register/',views.regi),
    path('',views.samp),
    path('login/loginsub/',views.sub),
]