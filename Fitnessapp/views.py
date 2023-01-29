from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Contact,Trainer,MembershipPlan,Enrollment,Attendance,Gallery
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def home(request):
    return render(request,'base.html')

def signup(request):
    
    if request.method=="POST":
        username= request.POST.get('mobile')
        first_name= request.POST.get('first_name')
        #last_name= request.POST.get('last_name')
        email= request.POST.get('email')
        pass1= request.POST.get('pass1')
        pass2= request.POST.get('pass2')

        if len(username)<10 or len(username)>10:
            messages.info(request,'Phone number must be in 10 digits')
            return redirect('/signup')

        if pass1 != pass2:
            messages.info(request,'Both passwords not match')
            return redirect('/signup')
        
        try:
            if User.objects.get(username=username):
                messages.warning(request,'Phone number is already taken')
                return redirect('/signup')
        except Exception as identifier:
            pass

        myuser=User.objects.create_user(username,email,pass1,first_name=first_name)
        myuser.save()
        messages.success(request,'User Created. Please Login')
        return redirect('/login')
    return render(request,'signup.html')    

def handlelogin(request):  # sourcery skip: move-assign
    if request.method=="POST":
        username= request.POST.get('mobile')
        pass1= request.POST.get('pass1')
        myuser=authenticate(username=username, password=pass1)
        context={"myuser":myuser}
        if myuser is not None:
            login(request,myuser)
            messages.info(request,'Login Successfull')
            #return redirect('/')
            return render(request,'base.html',context=context)
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('/login')   
    return render(request,'login.html')

def handlelogout(request):
    logout(request)
    messages.success(request,'Logout Successful')
    return redirect('/login')

def handlecontact(request):
    if request.method != "POST":
        return render(request,'contact.html')
    name= request.POST.get('fullname')
    email= request.POST.get('email')
    phonenumber= request.POST.get('mobile')
    description= request.POST.get('desc')
    mycontact=Contact(name=name, email=email, phonenumber=phonenumber, description=description)
    mycontact.save()
    messages.info(request,'Thank you contacting with us! Our excecutive call you within 24 Hrs.')
    return redirect('/contact')  

def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request,'please Login and Try Again')
        return redirect('/login')

    Membership=MembershipPlan.objects.all()
    SelectTrainer=Trainer.objects.all()
    context={"Membership":Membership,"SelectTrainer":SelectTrainer}
    if request.method=="POST":
        return _extracted_from_enroll_10(request)
    return render(request,'enrollment.html',context=context)    


# TODO Rename this here and in `enroll`
def _extracted_from_enroll_10(request):
    fullname= request.POST.get('FullName')
    email= request.POST.get('email')
    gender= request.POST.get('gender')
    phone_number= request.POST.get('PhoneNumber')
    DOB= request.POST.get('DOB')
    select_membership_plan= request.POST.get('member')
    select_trainer= request.POST.get('trainer')
    reference= request.POST.get('reference')
    address= request.POST.get('address')
    query=Enrollment(fullname=fullname,email=email,gender=gender,phone_number=phone_number,DOB=DOB,select_membership_plan=select_membership_plan,select_trainer=select_trainer,reference=reference,address=address)
    query.save()
    messages.success(request,"Thanks For Enrollment")
    return redirect('/join')    
        
def getattendance(request):
    if not request.user.is_authenticated:
        messages.error(request,'please Login and Try Again')
        return redirect('/login')
    SelectTrainer=Trainer.objects.all()
    context={"SelectTrainer":SelectTrainer}    
    phone_number= request.POST.get('PhoneNumber')
    login= request.POST.get('logintime')
    logout= request.POST.get('loginout')
    workout= request.POST.get('workout')
    trainer= request.POST.get('trainer')
    attendance=Attendance(phone_number=phone_number,login=login,logout=logout,workout=workout,trainer=trainer)
    attendance.save()
    print(attendance)
    messages.success(request,'attendance Add Successfully')
    return render(request,'attendance.html',context=context)    

def  getprofile(request):
    if not request.user.is_authenticated:
        messages.error(request,'please Login and Try Again')
        return redirect('/login')
    phone_user=request.user
    post=Enrollment.objects.filter(phone_number=phone_user)
    attendance=Attendance.objects.filter(phone_number=phone_user)
    context={'posts':post,'attendance':attendance}
    return render(request,'profile.html',context=context)        

def gallery(request):
    posts=Gallery.objects.all()
    context={"posts":posts}
    return render(request,"gallery.html",context)    