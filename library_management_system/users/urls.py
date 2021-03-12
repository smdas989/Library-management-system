from django.urls import path, include

from django.conf.urls import url
from .views import RegisterFormView, HomePageView, \
    LoginView, LogoutView, UserProfile, AdminProfile, \
    Students, UserDetailsView,  \
    Faculties, Librarians, ValidateUsernameView


urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('accounts/register/', RegisterFormView.as_view(), name='register'),
    path('accounts/student_login', LoginView.as_view(), name='login_user'),

    path('accounts/logout/',LogoutView.as_view(),name='logout'),
    path('user_profile/',UserProfile.as_view(),name='user_profile'),
    path('admin_page/',AdminProfile.as_view(), name='admin_page'),
    path('admin_page/students/',Students.as_view(), name='students'),
    path('admin_page/faculties/',Faculties.as_view(), name='faculties'),
    path('admin_page/librarians/',Librarians.as_view(), name='librarians'),
    path('user_details/<int:id>/',UserDetailsView.as_view(), name='user_details'), 
    path('validate_username/', ValidateUsernameView.as_view(), name='validate_username'),

]
