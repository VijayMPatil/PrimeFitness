from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=55)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=13)
    description=models.TextField()
    def __str__(self):
        return self.email

class Trainer(models.Model):
    name= models.CharField(max_length=55)
    gender= models.CharField(max_length=25)
    phone_number= models.CharField(max_length=25)
    salary= models.IntegerField(max_length=25)
    created_at= models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.name

class MembershipPlan(models.Model):
    plan= models.CharField(max_length=185)
    price= models.IntegerField(max_length=55)
    def __int__(self):
        return self.id

class Enrollment(models.Model):        
    fullname= models.CharField(max_length=55)
    email= models.EmailField()
    gender= models.CharField(max_length=55)
    phone_number= models.CharField(max_length=13)
    DOB= models.CharField(max_length=50)
    select_membership_plan= models.CharField(max_length=150)
    select_trainer= models.CharField(max_length=55)
    reference= models.CharField(max_length=60)
    address= models.TextField()
    paymentStatus= models.CharField(max_length=55,blank=True,null=True)
    price= models.IntegerField(max_length=55,blank=True,null=True)
    due_date= models.DateTimeField(blank=True,null=True)
    created_at= models.DateTimeField(auto_now_add=True,blank=True)

class Attendance(models.Model):
    phone_number= models.CharField(max_length=13,null=True,blank=True)
    login=models.CharField(max_length=50)
    logout=models.CharField(max_length=50)
    workout=models.CharField(max_length=100)
    trainer=models.CharField(max_length=100)
    created_at= models.DateTimeField(auto_now_add=True,null=True,blank=True)
    def __int__(self):
        return self.id    

class Gallery(models.Model):
    title= models.CharField(max_length=100)
    img= models.ImageField(upload_to='gallery')
    created_at= models.DateTimeField(auto_now_add=True,blank=True)
    def __int__(self):
        return self.id
