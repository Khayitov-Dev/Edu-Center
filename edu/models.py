from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL


class Day(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=255)
    days = models.ManyToManyField(Day,related_name="days")
    
    
    def __str__(self):
        return self.name




class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=True,related_name="teacher_profile")
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to="teacher/")
    phone = models.IntegerField()
    address = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True,blank=True,related_name="teachers")


    def __str__(self):
        return self.username




class Group(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL, null=True,blank=True,related_name="group")
    day = models.ManyToManyField(Day)
    start = models.TimeField()
    finish = models.TimeField()
    price = models.DecimalField(max_digits=10,decimal_places=2,default=200000.00)



    def __str__(self):
        return self.name


class Student(models.Model):
    STATUSS = (
        ("waiting","Waiting"),
        ("active","Active"),
    )
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to="student/")
    phone = models.IntegerField()
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=50,choices=STATUSS,default="waiting")
    group = models.ForeignKey(Group,on_delete=SET_NULL,null=True,blank=True,related_name="students")


    def __str__(self):
        return self.name