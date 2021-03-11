app_name = 'library'

from django.urls import path
from django.conf.urls import url
from .views import IssueBookView, ShowBookView, AddBookView, \
     UpdateBookView, DeleteBookView, ShowBookRecordView, ShowBookDetailsView ,\
    IncrementDecrementCopyView
    
urlpatterns = [
    path('show_book/', ShowBookView.as_view(), name='show_book'),
    path('show_book_record/', ShowBookRecordView.as_view(), name='show_book_record'),
    path('show_book_details/<int:id>/', ShowBookDetailsView.as_view(), name='show_book_details'),
    path('student_profile/issue_book/', IssueBookView.as_view(), name='issue_book'),
    path('admin_profile/add_book/', AddBookView.as_view(), name='add_book'),
    path('admin_profile/update_book/<int:id>/', UpdateBookView.as_view(), name='update_book'),
    path('admin_profile/delete_book/<int:id>/', DeleteBookView.as_view(), name='delete_book'),
    path('increment_decrement_book/', IncrementDecrementCopyView.as_view(), name='increment_decrement_book'),
    
]
