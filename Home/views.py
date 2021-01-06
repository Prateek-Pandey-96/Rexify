from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from Home.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json

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
    skills.delete()
    
    experiences = Experience.objects.filter(customer=customer)
    newExperiences=[]
    for experience in experiences:
        newExperiences.append({"JobTitle":experience.jobTitle,"FirmName":experience.firmName,"StartDate":experience.startDate.strftime('%F'),"EndDate":experience.endDate.strftime('%F'),"Name1":experience.project1,"Description1":experience.description1,"Name2":experience.project2,"Description2":experience.description2})
    experiences.delete()


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
        experiences = json.loads(request.POST.get("experiences"))

        for experience in experiences:
            try:
                check = Experience.objects.get(customer=customer,firmName=experience['FirmName'])
                if check is not None:
                    print("experience already exists")
            except:
                experienceObject = Experience(customer=customer,jobTitle=experience['JobTitle'],firmName=experience['FirmName'],startDate=experience['StartDate'],endDate=experience['EndDate']
                ,project1=experience['Name1'],description1=experience['Description1'],project2=experience['Name2'],description2=experience['Description2'])
                experienceObject.save()

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
        
        
            
    context = {'customer':customer, 'secondarySchool':secondarySchool, 'srSecondarySchool':srSecondarySchool,'college': college,'skills': newSkills,'experiences': newExperiences}
    
    return render(request, 'create.html', context)

@login_required(login_url='login')
def viewBasic(request,pk):
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
    experiences = Experience.objects.filter(customer=customer)
    context = {'customer': customer,'secondarySchool':secondarySchool, 'srSecondarySchool':srSecondarySchool,'college': college,'skills': skills,'experiences': experiences}     
    return render(request,'viewBasic.html', context)

@login_required(login_url='login')
def viewAvg(request,pk):
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
    experiences = Experience.objects.filter(customer=customer)
    context = {'customer': customer,'secondarySchool':secondarySchool, 'srSecondarySchool':srSecondarySchool,'college': college,'skills': skills,'experiences': experiences}     
    return render(request,'viewAvg.html', context)

@login_required(login_url='login')
def viewBest(request,pk):
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
    experiences = Experience.objects.filter(customer=customer)
    context = {'customer': customer,'secondarySchool':secondarySchool, 'srSecondarySchool':srSecondarySchool,'college': college,'skills': skills,'experiences': experiences}     
    return render(request,'viewBest.html', context)

@login_required(login_url='login')
def finalPage(request,pk):
        customer = Customer.objects.get(id = pk)
        data = {
             'customer': customer, 
             'secondarySchool' : SecondarySchool.objects.get(customer=customer),
             'srSecondarySchool' : SrSecondarySchool.objects.get(customer=customer),
             'college' : College.objects.get(customer=customer),
             'skills': Skill.objects.filter(customer=customer),
             'experiences' : Experience.objects.filter(customer=customer)
        }
        return render(request, 'finalPage.html',data)

@login_required(login_url='login')
def finalPage2(request,pk):
        customer = Customer.objects.get(id = pk)
        data = {
             'customer': customer, 
             'secondarySchool' : SecondarySchool.objects.get(customer=customer),
             'srSecondarySchool' : SrSecondarySchool.objects.get(customer=customer),
             'college' : College.objects.get(customer=customer),
             'skills': Skill.objects.filter(customer=customer),
             'experiences' : Experience.objects.filter(customer=customer)
        }
        return render(request, 'finalPage2.html',data)
    
@login_required(login_url='login')
def finalPage3(request,pk):
        customer = Customer.objects.get(id = pk)
        data = {
             'customer': customer, 
             'secondarySchool' : SecondarySchool.objects.get(customer=customer),
             'srSecondarySchool' : SrSecondarySchool.objects.get(customer=customer),
             'college' : College.objects.get(customer=customer),
             'skills': Skill.objects.filter(customer=customer),
             'experiences' : Experience.objects.filter(customer=customer)
        }
        return render(request, 'finalPage3.html',data)

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

@login_required(login_url='login')
def myResumes(request):
    resumes = Resume.objects.filter(user=request.user)
    context = { 'resumes':resumes}
    return render(request, 'myResumes.html',context)