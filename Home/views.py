from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from Home.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json
from copy import deepcopy

def loginPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate( request, username= username, password = password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request, "Username or Password is incorrect")
        context={}
        return render(request, 'login.html', context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account was created for " + user)
                return redirect('login')
        context = {'form': form}
        return render(request, 'register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    # context is a set of vaiables sent to a template
    context = {

    }
    return render(request, 'index.html', context)

@login_required(login_url='login')
def templates(request):
    return render(request, 'template.html')

@login_required(login_url='login')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('senderName')
        email = request.POST.get('senderEmail')
        query = request.POST.get('senderQuery')
        contact = Contact(name= name, email= email, query= query, date= datetime.today())
        contact.save()
    return render(request, 'contact.html')

@login_required(login_url='login')
def create(request,pk):
    customer = Customer.objects.get(id = pk)
    try:
        secondarySchool = SecondarySchool.objects.get(customer=customer)
    except:
        secondarySchool = SecondarySchool()
    try:
        srSecondarySchool = SrSecondarySchool.objects.get(customer=customer)
    except:
        srSecondarySchool = SrSecondarySchool()
    try:
        college = College.objects.get(customer=customer)
    except:
        college = College()

    skills = Skill.objects.filter(customer=customer)
    newSkills = []
    for skill in skills:
        newSkills.append({"Name":skill.skillName,"Value":skill.proficiency})
        print(newSkills)
    skills.delete()
    
    if request.method == "POST":
        institutionName = request.POST.get("secondarySchoolName")
        passingYear = request.POST.get("secondarySchoolPassingYear")
        cityName = request.POST.get("secondarySchoolCityName")
        branch = request.POST.get("secondarySchoolBranchName")
        institutionName2 = request.POST.get("srSecondarySchoolName")
        passingYear2 = request.POST.get("srSecondarySchoolPassingYear")
        cityName2 = request.POST.get("srSecondarySchoolCityName")
        branch2 = request.POST.get("srSecondarySchoolBranchName")
        institutionName3 = request.POST.get("collegeName")
        passingYear3 = request.POST.get("collegePassingYear")
        cityName3 = request.POST.get("collegeCityName")
        branch3 = request.POST.get("collegeBranchName")
        skills = json.loads(request.POST.get("skills"))
        print(json.loads(request.POST.get("experiences")))
        
        for skill in skills:
            try:
                check = Skill.objects.get(customer=customer,skillName=skill['Name'])
                if check is not None:
                    print("skill already exists")
            except:
                skillObject = Skill(customer=customer,skillName=skill['Name'],proficiency=skill['Value'])
                skillObject.save()
        
        
        try:
            secondarySchool = SecondarySchool(customer=customer,passingYear=passingYear,institutionName=institutionName,cityName=cityName,branch=branch)
            secondarySchool.save()
        except:            
            secondarySchool = SecondarySchool.objects.get(customer=customer)
            secondarySchool.institutionName = request.POST.get("secondarySchoolName")
            secondarySchool.passingYear = request.POST.get("secondarySchoolPassingYear")
            secondarySchool.cityName = request.POST.get("secondarySchoolCityName")
            secondarySchool.branch = request.POST.get("secondarySchoolBranchName")
            secondarySchool.save()
            
        try:            
            srSecondarySchool =SrSecondarySchool(customer=customer,passingYear=passingYear2,institutionName=institutionName2,cityName=cityName2,branch=branch2)
            srSecondarySchool.save()
        except:
            srSecondarySchool = SrSecondarySchool.objects.get(customer=customer)
            srSecondarySchool.institutionName = request.POST.get("srSecondarySchoolName")
            srSecondarySchool.passingYear = request.POST.get("srSecondarySchoolPassingYear")
            srSecondarySchool.cityName = request.POST.get("srSecondarySchoolCityName")
            srSecondarySchool.branch = request.POST.get("srSecondarySchoolBranchName")
            srSecondarySchool.save()

        try:
            college = College(customer=customer,passingYear=passingYear3,institutionName=institutionName3,cityName=cityName3,branch=branch3)
            college.save()
        except:
            college = College.objects.get(customer=customer)
            college.institutionName = request.POST.get("collegeName")
            college.passingYear = request.POST.get("collegePassingYear")
            college.cityName = request.POST.get("collegeCityName")
            college.branch = request.POST.get("collegeBranchName")
            secondarySchool.save()
        
        
            
    context = {'customer':customer, 'secondarySchool':secondarySchool, 'srSecondarySchool':srSecondarySchool,'college': college,'skills': newSkills}
    
    return render(request, 'create.html', context)



@login_required(login_url='login')
def viewResume(request):       
    return render(request,'viewResume.html')

@login_required(login_url='login')
def intermediate(request):
    if request.method == "POST":
        name = request.POST.get('customerName')
        email = request.POST.get('customerEmail')
        job = request.POST.get('customerJob')
        phone = request.POST.get('customerPhone')
        objective = request.POST.get('customerObjective')
        user = request.user
        customer = Customer(user=user,name = name, email= email, job= job, phone= phone, objective= objective, date= datetime.today())
        customer.save()
        return redirect('create',customer.pk)
    return render(request, 'intermediate.html')
