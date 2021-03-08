from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User, Role
from library.models import BookRecord, Books

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
            
            password = form.cleaned_data['password']
            abc = form.save(commit=False)
            abc.set_password(password)
            abc.save()
            # if form.cleaned_data['role'] == 'Student':
            #     return redirect('/student_profile')
            # elif form.cleaned_data['role'] == 'Faculty':
            #     return redirect('/faculty_profile')
            # elif form.cleaned_data['role'] == 'Librarian':
            #     return redirect('/librarian_profile')
            # else:
            #     return redirect('/admin_profile')
            return redirect('/accounts/login')
        else:
            messages.error(request, 'Username already exists')
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
            elif user.role.role == 'Faculty':
                return redirect('/faculty_profile')
            elif user.role.role == 'Librarian':
                return redirect('/librarian_profile')
            else:
                return redirect('/student_profile')
        else:
            messages.error(request, 'Invalid Credentials')
            return HttpResponseRedirect(settings.LOGIN_URL)

class LogoutView(View):
     def get(self, request):
        logout(request)
        return redirect('/accounts/login')

class StudentProfile(LoginRequiredMixin, View):
    def get(self, request):

        user = User.objects.get(username=request.user)
       
        bookrecords = BookRecord.objects.filter(borrower_name=user)
        # book_name = Books.objects.get(id=BookRecord.objects.get(borrower_name=user))
       
        return render(request, "student_profile.html",{'bookrecords':bookrecords})

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

class StudentDetailsView(LoginRequiredMixin, View):
    def get(self, request,id):
        student = User.objects.filter(id=id).first()
        return render(request, "student_details.html",{'student':student})

class LibrarianProfile(LoginRequiredMixin, View):
    def get(self, request):

        user = User.objects.get(username=request.user)
       
        bookrecords = BookRecord.objects.filter(borrower_name=user)
        # book_name = Books.objects.get(id=BookRecord.objects.get(borrower_name=user))
       
        return render(request, "librarian_profile.html",{'bookrecords':bookrecords})


class LibrarianDetailsView(LoginRequiredMixin, View):
    def get(self, request,id):
        librarian = User.objects.filter(id=id).first()
        return render(request, "librarian_details.html",{'librarian':librarian})


class FacultyProfile(LoginRequiredMixin, View):
    def get(self, request):

        user = User.objects.get(username=request.user)
       
        bookrecords = BookRecord.objects.filter(borrower_name=user)
        # book_name = Books.objects.get(id=BookRecord.objects.get(borrower_name=user))
       
        return render(request, "faculty_profile.html",{'bookrecords':bookrecords})

class FacultyDetailsView(LoginRequiredMixin, View):
     def get(self, request,id):
        faculty = User.objects.filter(id=id).first()
        return render(request, "faculty_details.html",{'faculty':faculty})