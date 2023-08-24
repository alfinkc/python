from django.shortcuts import render,redirect
# from django.contrib import message
from django.contrib.auth.models import User,auth
# from django.contrib.auth.hashers import make_password,check_password
# from.models import userpassword
from .models import places
# from .models import userpassword
from django.contrib.auth import authenticate,login,logout
# print(make_password('1234'))
# print(check_password('1234'))
from django.contrib.auth import authenticate,login


# Create your views here.
def index(request):
    pics=places.objects.all()
    return render(request,'index.html',{'pics':pics})

# def fun(request):
#     obj=places.objects.all()
#     return render(request,'index.html',{'star':obj})
    


def register(request):

    if request.method=="POST":
        username=request.POST['uname']
        first_name=request.POST['fname']
        last_name = request.POST['lname']
        email= request.POST['email']
        password=request.POST['password']
        confirm_your_password = request.POST['confirm your password']
        user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password).save()
        # userpassword(username=username,password=password).save()

        print('user created')
        return redirect('register')
      
        




    

    else:
        return render(request,'register.html')

        
        

            

    
    
    
       

    




def login1(request):
    if request.method=="POST":
        username=request.POST['uname']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            login(request,user)

            return redirect('userhome')
        else:
            return redirect('login1')
    else:
        return render(request,'login.html')  

def userhome(request):
    return render(request,'userhome.html') 



def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html')
    else:
        return redirect('userhome')

def update(request,pk):
    getdata=User.objects.get(id=pk)
    

    return render(request,'update.html',{'key':getdata})


def updatedata(request,pk):
    udate=User.objects.get(id=pk)
    udate.username = request.POST['uname']
    udate.first_name=request.POST['fname']
    udate.last_name=request.POST['lname']
    udate.email=request.POST['email']
    udate.save()
    return redirect('profile')


def delete(request,pk):
    if request.method=='POST':
        obj=User.objects.get(id=pk)
        obj.delete()
        return redirect('register')
    return render(request,'delete.html')    


    
    

    
