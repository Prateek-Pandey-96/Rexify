from django.db import models
from django.conf import settings


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    query = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    job = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    objective = models.TextField()
    date = models.DateField()

    # def __str__(self):
    #     return self.name
    

class SecondarySchool(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, unique=True)
    institutionName = models.CharField(max_length=100)
    passingYear = models.CharField(max_length=5)
    cityName = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return self.institutionName

class SrSecondarySchool(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, unique=True)
    institutionName = models.CharField(max_length=100)
    passingYear = models.CharField(max_length=5)
    cityName = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return self.institutionName

class College(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, unique=True)
    institutionName = models.CharField(max_length=100)
    passingYear = models.CharField(max_length=5)
    cityName = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return self.institutionName

class Experience(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    jobTitle = models.CharField(max_length=50)
    firmName = models.CharField(max_length=50)
    startDate = models.DateField()
    endDate = models.DateField()
    project1 = models.CharField(max_length=100)
    description1 = models.TextField()
    project2 = models.CharField(max_length=100)
    description2 = models.TextField()


class Skill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    skillName = models.CharField(max_length=50)
    proficiency = models.CharField(max_length=20)

class Resume(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete = models.SET_NULL)
    customer = models.ForeignKey(Customer , null = True, on_delete = models.SET_NULL)
    date = models.DateField()
