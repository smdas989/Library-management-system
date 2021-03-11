from django.urls import path, include
from django.conf.urls import url
from .views import RegisterFormView, HomePageView, \
    LoginView, LogoutView, StudentProfile, AdminProfile, \
    Students, StudentDetailsView, LibrarianProfile, \
    LibrarianDetailsView, FacultyProfile, \
    FacultyDetailsView, Faculties, Librarians, ValidateUsernameView
    # ValidateUsernameView



urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('accounts/register/', RegisterFormView.as_view(), name='register'),
    path('accounts/student_login', LoginView.as_view(), name='login_user'),

    path('accounts/logout/',LogoutView.as_view(),name='logout'),
    path('student_profile/',StudentProfile.as_view(),name='student_profile'),
    path('librarian_profile/',LibrarianProfile.as_view(),name='librarian_profile'),
    path('faculty_profile/',FacultyProfile.as_view(),name='faculty_profile'),

    path('admin_page/',AdminProfile.as_view(), name='admin_page'),
    path('admin_page/students/',Students.as_view(), name='students'),
    path('admin_page/faculties/',Faculties.as_view(), name='faculties'),
    path('admin_page/librarians/',Librarians.as_view(), name='librarians'),
    path('student_profile/<int:id>/',StudentDetailsView.as_view(), name='student_details'),
    path('faculty_profile/<int:id>/',FacultyDetailsView.as_view(), name='faculty_details'),

    path('librarian_profile/<int:id>/',LibrarianDetailsView.as_view(), name='librarian_details'),

    path('validate_username/', ValidateUsernameView.as_view(), name='validate_username'),

]
