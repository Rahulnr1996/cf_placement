from django.shortcuts import render
from . models import *

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def reg(request):
    if request.method=='POST':
        usrnm=request.POST.get('username')
        eml=request.POST.get('email')
        phn=request.POST.get('phone')
        pswd=request.POST.get('password')
        obj=register.objects.create(name=usrnm,email=eml,phone=phn,password=pswd)
        
        if obj:
            obj.save()
            return render(request,"regsuccess.html",{'msg':'success'})
        else:
            return render(request,"registration.html",{'msg':'not'})
    else:
        return render(request,'registration.html',{'msg':''})





def login(request):
    if request.method=='POST':
        eml=request.POST.get('email')
        pswd=request.POST.get('password')
        obj=register.objects.filter(email=eml,password=pswd)
        
        if obj:
            request.session['email']=eml
            request.session['paswd']=pswd
            return render(request,"index.html",{'msg':'success'})
        else:
            request.session['email']=''
            request.session['paswd']=''
            return render(request,"login.html",{'msg':'not'})
    else:
        return render(request,'login.html',{'msg':''})