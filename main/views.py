from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import CustomUser, DonatedMeds, GetMeds
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def donatemed(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            medicine_name=request.POST['medicine_name']
            full_name = request.POST['full_name']
            med_photo = request.FILES['med_photo']
            expiry_date = request.POST['expiry_date']
            email = request.POST['email']
            phone = request.POST['phone']
            location1 = request.POST['location1']
            location2 = request.POST['location2']
            location3 = request.POST['location3']
            donated_by = request.user.username
            received = False

            donate = DonatedMeds(medicine_name=medicine_name, med_photo=med_photo, expiry_date=expiry_date, full_name=full_name, email=email, phone=phone, location1=location1, location2=location2, location3=location3, donated_by=donated_by, received=False)
            donate.save()
            messages.success(request, "Successfully Donated A Medicine, Thankyou!")
            return redirect('/')
    else:
        messages.error(request, "Please Create An Account Or Login To Donate a Medicine!")
        return redirect('/')

def donatetemplate(request):
    return render(request, 'donate.html')

def getmedtemplate(request):
    meds = DonatedMeds.objects.filter(received=True)
    return render(request, 'buy.html', {'meds':meds})

def getmed(request):
    if DonatedMeds.objects.filter(donated_by=request.user.username).exists():
        if request.method == "POST":
            medicine_name=request.POST['medicine_nameget']
            location1 = request.POST['location1get']
            location2 = request.POST['location2get']
            location3 = request.POST['location3get']
            full_name = request.POST['nameget']
            email = request.POST['emailget']
            phone = request.POST['phoneget']
            received = False
            print("success")
            getmed1234 = GetMeds(medicine_name=medicine_name, location1=location1, location2=location2, location3=location3, full_name=full_name, email=email, phone=phone, received=False)
            getmed1234.save()
            messages.success(request, "Successfully Ordered The Medicine!")
            return redirect('/')
    else:
        messages.error(request, "To Order Medicines, Please Donate a Medicine!")            
        return redirect('/')
def home(request):
    return render(request, 'home.html')

def Logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Successfully Logged In")
        return redirect('/')
    else:
        messages.error(request, "You are not logged in!")
        return redirect('/')

def Login(request):
    return render(request, 'login.html')

def HandleLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In!")
            return redirect('/')
        else:
            messages.error(request, "Incorrect Email Or Password!")
            return redirect('/')

def HandleSignUp(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        phone = request.POST['phone']
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "User with that username already exists!")
            return redirect('/signup')
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "User with that email already exists! Please choose another email")
            return redirect('/signup')
        elif len(password1) < 7:
            messages.error(request, "The length of the password should atleast be 7 characters")
            return redirect('/signup')
        elif len(username) < 5:
            messages.error(request, "The length of the username should atleast be 5 characters")
            return redirect('/signup')
        elif len(username) > 13:
            messages.error(request,"The length of the username should be less than 13 characters")
            return redirect('/signup')
        elif len(username) > 15:
            messages.error(request,"The length of the password should be less than 15 characters")
            return redirect('/signup')
        elif password1!=password2:
            messages.error(request,"Passwords do not match!")
            return redirect('/signup')
        elif not(phone.isnumeric()):
            messages.error(request,"Please enter a vaild phone number!")
            return redirect('/signup')
        elif len(phone) != 10:
            messages.error(request,"There should be 10 digits in the phone number!")
            return redirect('/signup')
        else:
            u = CustomUser(username=username, password=password1, email=email, first_name=first_name, last_name=last_name, phone_number=phone)
            u.save()
            messages.success(request, "Successfully Created An Account!")
            return redirect('/')

def SignUp(request):
    return render(request, 'signup.html')