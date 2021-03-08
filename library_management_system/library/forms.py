from django import forms
from .models import Books

class BookAddForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title','author','no_of_copies','no_of_available_copies','genre','book_image']
   
