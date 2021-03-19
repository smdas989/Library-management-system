from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User, Role, Student, Faculty, Admin, Librarian
from library.models import BookRecord, Books
from django.http import JsonResponse
from django.conf import settings 
from django.core.mail import send_mail 

class HomePageView(View):
    def get(self, request):
        return render(request, "home_page.html")

class RegisterFormView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, "registration.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form=RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            
            role = form.cleaned_data['role'].role
            if role == 'Admin':
                Admin.objects.create(user=user)
            elif role == 'Student':
                Student.objects.create(user=user)
            elif role == 'Faculty':
                Faculty.objects.create(user=user)    
            elif role == 'Librarian':
                Librarian.objects.create(user=user)                     
            else:
                return redirect('/accounts/register')

            #User login
            login(request,user)

            #redirecting to desired profile
            if role == 'Admin':
                return redirect('/admin_page')
            else:
                return redirect('/user_profile')
        else:
            messages.error(request, form.errors)
        return redirect('/accounts/register')
        
       
class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
       
        user = authenticate(request,username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            if user.role.role == 'Admin':
                return redirect('/admin_page')
            else:
                return redirect('/user_profile')
        else:
            messages.error(request, 'Invalid Credentials')
            return HttpResponseRedirect(settings.LOGIN_URL)

class LogoutView(View):
     def get(self, request):
        logout(request)
        return redirect('/accounts/login')

class UserProfile(LoginRequiredMixin, View):
    def get(self, request):
        user = User.objects.get(username=request.user)
        role = user.role.role
        bookrecords = BookRecord.objects.filter(borrower_name=user)
        context = {
            'bookrecords':bookrecords,
            'role':role,
            }
        return render(request, "user_profile.html",context)

class AdminProfile(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "admin_profile.html")

class Students(LoginRequiredMixin, View):
    def get(self, request):
        role = Role.objects.get(role='Student')
        students = User.objects.filter(role=role)
        return render(request, "students.html",{'students':students})

class Faculties(LoginRequiredMixin, View):
    def get(self, request):
        role = Role.objects.get(role='Faculty')
        faculties = User.objects.filter(role=role)
        return render(request, "faculties.html",{'faculties':faculties})

class Librarians(LoginRequiredMixin, View):
    def get(self, request):
        role = Role.objects.get(role='Librarian')
        librarians = User.objects.filter(role=role)
        return render(request, "librarians.html",{'librarians':librarians})

class UserDetailsView(LoginRequiredMixin, View):
    def get(self, request,id):
        user = User.objects.filter(id=id).first()
        return render(request, "user_details.html",{'user':user})

class ValidateUsernameView(View):
    def get(self, request):
        username=request.GET.get("username")
        user_obj=User.objects.filter(username=username).exists()
        if user_obj:
            return HttpResponse(True)
        else:
            return HttpResponse(False)