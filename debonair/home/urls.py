from django.urls import path
from . import views 

urlpatterns = [
    
    path('test/',views.samp),
    path('login/',views.sam,name='login_page'),
    path('register/',views.regi,name='register_page'),
    path('',views.samp,name='homepage'),
    path('login/loginsub/',views.sub,name='loginpage2'),
    path('logout/',views.logout),
]