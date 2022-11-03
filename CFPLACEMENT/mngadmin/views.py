from django.shortcuts import render,redirect
from . models import *

# Create your views here.
def mlogin(request):
    if request.method=='POST':
        usr=request.POST.get('usrnm')
        pswd=request.POST.get('password')
        obj=mregister.objects.filter(name=usr,password=pswd)
        if obj:
            request.session['name']=usr
            request.session['pswd']=pswd
            # for ls in obj:
            #     idno=ls.id
            #     request.session['idn']=idno
            return render(request,'managementHome.html')
        else:
            request.session['name']=''
            request.session['pswd']=''
            return render(request,'mnglogin.html')
    else:

        return render(request,'mnglogin.html')

#management detail page

def details(request):
    if request.method=='POST':
        clg=request.POST.get('cn')
        lcn=request.POST.get('lc')
        obj=mdetails.objects.create(clgname=clg,location=lcn)
        if obj:
            obj.save()
            return render(request,'managementDataView.html')
        else:
            return render(request,'management.html')
    else:
        return render(request,'management.html')






#management detail list view
def mdetail(request):
    obj=mdetails.objects.all()
    return render(request,"managementDataView.html",{"data":obj})


#management detail view edit


def edit(request):
    idno=request.GET.get('idn')
    obj=mdetails.objects.filter(id=idno)
    return render(request,"managementDataViewUpdate.html",{"data":obj})

#management detail view update

def update(request):
    if request.method=="POST":
        idn=request.POST.get("idl")
        cn=request.POST.get("clg1")
        lcn=request.POST.get("lcn1")
        obj=mdetails.objects.get(id=idn)
        obj.clgname=cn
        obj.location=lcn
        obj.save()
        return redirect("/madmin/mdetailsview")

#management detail view delete

def delete(request):
    idno=request.GET.get('idn')
    obj=mdetails.objects.filter(id=idno) 
    obj.delete()
    return redirect("/madmin/mdetailsview")



#company details add
def companyadd(request):
    if request.method=="POST":
        cn=request.POST.get("cn")
        cl=request.POST.get("cl")
        cv=request.POST.get("cv")
        nv=request.POST.get("nv")
        cd=request.POST.get("cd")
        obj=mcompanyT.objects.create(cname=cn,clocation=cl,cvacancy=cv,nvacancy=nv,cdate=cd)
        if obj:
            obj.save()
            return render(request,"managementcompanyview.html")
        else:
            return render(request,"managementcompanyadd.html")
    else:
        return render(request,"managementcompanyadd.html")

    
    


#company details view
def mcompany(request):
    obj=mcompanyT.objects.all()
    return render(request,"managementcompanyview.html",{"data":obj})

def cedit(request):
    idno=request.GET.get('idn')
    obj=mcompanyT.objects.filter(id=idno)
    return render(request,"managementcompanyupdate.html",{"data":obj})

#management detail view update

def cupdate(request):
    if request.method=="POST":
        idn=request.POST.get("idl")
        cn=request.POST.get("cn")
        cl=request.POST.get("cl")
        cv=request.POST.get("cv")
        nv=request.POST.get("nv")
        cd=request.POST.get("cd")
        obj=mcompanyT.objects.get(id=idn)
        obj.cname=cn
        obj.clocation=cl
        obj.cvacancy=cv
        obj.nvacancy=nv
        obj.cdate=cd
        obj.save()
        return redirect("/madmin/companydata")

#management detail view delete

def cdelete(request):
    idno=request.GET.get('idn')
    obj=mcompanyT.objects.filter(id=idno) 
    obj.delete()
    return redirect("/madmin/companydata")


