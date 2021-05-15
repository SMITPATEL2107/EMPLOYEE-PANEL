from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from .models import *
from random import randint

# Create your views here.

def Register(request):
    return render(request,"login/index.html")
    
def Loginpage(request):
    return render(request,"login/loginpage.html")

def AddUser(request):
    try:
        firstname =request.POST['firstname']
        lastname = request.POST['lastname']
        birthday = request.POST['birthday']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        reapeatpassword = request.POST['reapeatpassword']
        user = User.objects.filter(email=email)
        if user:
                print("--------------2---------------")
                message = 'This email already exists'
                return render(request,("login/index.html"), {'message': message})
        else:
            if password == reapeatpassword:
                print("--------------3---------------")
                employeeid = randint(100000,9999999)
                newuser = User.objects.create(
                    email=email, password=password,employeeid=employeeid)
                newcust = customer.objects.create(user_id=newuser,firstname=firstname,lastname=lastname,birthday=birthday ,phone=phone)
                return render(request,("login/loginpage.html"))
            else:
                print("--------------4---------------")
                message = "Password and confirm password doesn't match"
                return render(request,("login/index.html"),{'message': message})
    except Exception as e1 :
        print("the error is--->",e1)

def Loginuser(request):
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.filter(email=email)
    print(user)
    if user:
        print("---enter-----")
        if user[0].password == password:
            # return render(request,("login/table.html"))
            # HttpResponseRedirect(reverse('showdata'))
            return redirect('showdata')
        else:
            message = "Your password is incorrect or user doesn't exist"
            return render(request, ("login/loginpage.html"), {'message': message})
    else:
        message = "user doesn't exist"
        return render(request, ("login/loginpage.html"), {'message': message})     

def ShowData(request):
    alldata =customer .objects.all()
    return render(request,"login/table.html",{'key1':alldata})

# def Photo(request):
#     Photo=request.FILES['Photo']
#     newphoto=pics.objects.create(photo=photo)
#     use=pics.object.get(photo=photo)
#     if user:
#         return render(request,("login/sorry.html"))
#     else:
#         return render(request,("login/show.html"))

def GetById(request,pk):
    getdata = customer.objects.get(pk=pk)
    return render(request,"login/editpage.html",{'key2':getdata})

def GetById1(request,pk):
    getdata1 = User.objects.get(pk=pk)
    return render(request,"login/editadmin.html",{'key3':getdata1})

def GetById2(request,pk):
    getdata2 = User.objects.get(pk=pk)
    return render(request,"login/showmail.html",{'key4':getdata2})

def Update(request,pk):
    udata=customer.objects.get(pk=pk)
    udata.firstname=request.POST['firstname']
    udata.lastname=request.POST['lastname']
    udata.birthday=request.POST['birthday']
    udata.phone=request.POST['phone']
    udata.save()
    return redirect('showdata')

def UpdateAdmin(request,pk):
    updata=User.objects.get(pk=pk)
    updata.email=request.POST['email']
    updata.password=request.POST['password']
    updata.save()
    return redirect('showdata')

def Delete(request,pk):
    try:
        print("-----enter in delete-----")
        ddata=customer.objects.get(pk=pk)
        ddata.delete()
        return redirect('showdata')
    
    except Exception as e2 :
        print("the error is--->",e2)
