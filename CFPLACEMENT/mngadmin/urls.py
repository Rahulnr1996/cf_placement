from django.urls import path
from . import views

urlpatterns = [
    path('mlogin',views.mlogin),
    path('mdetails',views.details),
    path('mdetailsview',views.mdetail),
    path('medit',views.edit),
    path('mupdate',views.update),
    path('mdelete',views.delete),



    path('companydata',views.mcompany),
    path('cedit',views.cedit),
    path('cupdate',views.cupdate),
    path('cdelete',views.cdelete),

]