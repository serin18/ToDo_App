from django.shortcuts import render,redirect
from django.views.generic import View
from reminder.forms import Register,signin,Taskform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from reminder.models import Task
from django.utils.decorators import method_decorator



def signin_requerd(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            return fn(request,*args,**kwargs)
    return wrapper


def mylogin(fn):
    def wrapper(request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Task.objects.get(id=id)
        if obj.user != request.user:
            return redirect("login")
        else:
            return fn(request,*args,**kwargs)
    return wrapper


# Create your views here.

class Homeview(View):
     def get (self,request,*args,**kwargs):
         return render (request,"front.html")


class Registerview(View):
    def get (self,request,*args,**kwargs):
        form=Register()
        return render (request,"reg.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=Register(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
        form=Register()
        return render(request,"reg.html",{"form":form})
        
        
    
class signviw(View):
    def get (self,request,*args,**kwargs):
        form=signin()
        return render (request,"login.html",{"form":form})
    
    def post (self,request,*args,**kwargs):
        form=signin(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_obj=authenticate(request,username=u_name,password=pwd)
            if user_obj:
                print("valied")
                login (request,user_obj)
                return redirect("table")
            else:
                    print("invalid")
        return render (request,"reg.html",{"form":form})
@method_decorator(signin_requerd,name="dispatch")
class taskview(View):
    def get(self,request,*args,**kwargs):
        form=Taskform()
        data=Task.objects.filter(user=request.user).order_by('complete')
        return render(request,"index.html",{"form":form,"data":data})
        
    def post(self,request,*args,**kwargs):
        form=Taskform(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
        else:
            print("invalid")
        form=Taskform()
        return render(request,"index.html",{"form":form})
    
class Tableview(View):
    def get(self,request,*args,**kwargs):
        
        data=Task.objects.filter(user=request.user).order_by('complete')
        return render(request,"table.html",{"data":data})
    
    def post(self,request,*args,**kwargs):
        form=Taskform(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
        else:
            print("invalid")
        form=Taskform()
        return render(request,"table.html",{"form":form})




@method_decorator(mylogin,name="dispatch")
class Taskupdate(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Task.objects.get(id=id)
        if qs.complete == True:
            qs.complete = False
            qs.save()
        elif qs.complete == False:
            qs.complete = True
            qs.save()


        return redirect ("table")
@method_decorator(mylogin,name="dispatch")   
class Taskdelete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Task.objects.filter(id=id).delete()
        return redirect ("table")

class Signout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")


