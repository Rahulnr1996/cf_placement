from django.urls import path
from . import views

urlpatterns=[
   
    
    path('adminlogin',views.alogin),
    path('reg',views.reg),

]