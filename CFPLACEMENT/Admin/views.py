from django.shortcuts import render
from . models import Adlogin
from CAMERIN . views import reg

# Create your views here.
def alogin(request):
    if request.method=='POST':
        usr=request.POST.get('usrnm')
        pswd=request.POST.get('password')
        obj=Adlogin.objects.filter(username=usr,password=pswd)
        if obj:
            request.session['usrname']=usr
            request.session['paswd']=pswd
            return render(request,"adminhome.html",{'msg':'success'})
        else:
            request.session['email']=''
            request.session['paswd']=''
            return render(request,"adlogin.html",{'msg':'not'})
    else:
        return render(request,'adlogin.html',{'msg':''})

        #management detail list view
def regsuccess(request):
    obj=register.objects.all()
    return render(request,"regsuccess.html",{"data":obj})