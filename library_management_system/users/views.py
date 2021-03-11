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
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.save()

            #User login
            login(request,user)

            #Sending email to the user
            subject = 'You have been registered'
            message = f'Hi {user.username}, thank you for registering in Library management system.'
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = ['smdas989@gmail.com', ] 
            send_mail( subject, message, email_from, recipient_list, fail_silently=False, ) 

            #redirecting to desired profile
            if form.cleaned_data['role'].role == 'Student':
                return redirect('/student_profile')
            elif form.cleaned_data['role'].role == 'Faculty':
                return redirect('/faculty_profile')
            elif form.cleaned_data['role'].role == 'Librarian':
                return redirect('/librarian_profile')
            else:
                return redirect('/admin_page')
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

# class ValidateUsernameView(View):
#     def post(self, request):

#         username = request.POST.get('username', None)
#         print(username)
#         data = {
#             'is_taken': User.objects.filter(username__iexact=username).exists()
#         }
#         return JsonResponse(data)

class ValidateUsernameView(View):
    def get(self, request):
        username=request.GET.get("username")
        user_obj=User.objects.filter(username=username).exists()
        if user_obj:
            return HttpResponse(True)
        else:
            return HttpResponse(False)