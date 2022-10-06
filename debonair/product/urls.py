from django.urls import path
from . import views


urlpatterns=[
    path('',views.details,name="details_page"),
    path('cmt/',views.commenting,name='commentbox'),
    path('search/',views.searching,name="searchbox")
    ] 