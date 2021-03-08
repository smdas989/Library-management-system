from django.db import models
from django.contrib.auth.models import AbstractUser, User
from phonenumber_field.modelfields import PhoneNumberField

class Role(models.Model):
    TYPE_CHOICES = (
        ('Student', 'Student'),
        ('Faculty', 'Faculty'),
        ('Librarian', 'Librarian'),
        ('Admin', 'Admin'),
    )
    role = models.CharField(max_length=255, choices=TYPE_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.role

class Department(models.Model):
    DEPARTMENT_CHOICES = (
        ('Computer_Engineering', 'Computer_Engineering'),
        ('Information_Technology', 'Information_Technology'),
        ('Mechanical_Engineering', 'Mechanical_Engineering'),
        ('Electronics_Engineering', 'Electronics_Engineering'),
        ('Civil_Engineering', 'Civil_Engineering'),
        ('Electrical_Engineering', 'Electrical_Engineering'),
      
    )
    department = models.CharField(max_length=255, choices=DEPARTMENT_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.department


class User(AbstractUser):
    department = models.ForeignKey(Department,on_delete=models.CASCADE, null=True, blank=True)
    contact_no = PhoneNumberField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to ='media/user/',null=True, blank=True) 
    role = models.ForeignKey(Role,on_delete=models.CASCADE, null=True, blank=True)


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class Faculty(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class Librarian(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class Admin(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

