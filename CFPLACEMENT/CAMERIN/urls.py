
from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('about',views.about),
    # path('reg',views.reg),
    path('log',views.login),
]