from django.shortcuts import render, redirect
from django.views import View
from .models import Books, BookRecord
from .forms import BookAddForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ShowBookView(LoginRequiredMixin, View):
    def get(self, request):
        books = Books.objects.all()
        return render(request, "allbooks.html",{'books':books})
class IssueBookView(LoginRequiredMixin, View):
    def get(self, request):

        #Check if book is available
        # Books.objects.
       
        books = Books.objects.all()
        

        return redirect('/show_book')

class ShowBookRecordView(LoginRequiredMixin, View):
    def get(self, request):
        bookrecords = BookRecord.objects.all()
        return render(request, "show_book_record.html",{'bookrecords':bookrecords})
        

class AddBookView(LoginRequiredMixin, View):
    def get(self, request):
        form = BookAddForm()
        return render(request, "add_books.html",{'form':form})

    def post(self,request):
        form=BookAddForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
           return redirect('/show_book')
        else:
            # messages.error(request, 'Username already exists')
            return redirect('/add_book')

class UpdateBookView(LoginRequiredMixin, View):
    def get(self, request,id):
        try:
            book = Books.objects.get(id=id)
        except Books.DoesNotExist:
            return redirect('/show_book')
        form = BookAddForm(instance=book)
        return render(request, "add_books.html",{'form':form})

    def post(self,request,id):
        book = Books.objects.get(id=id)
        form = BookAddForm(request.POST, instance=book)
        
        if form.is_valid():
           book = form.save(commit=False)
           book.save()
           return redirect('/show_book')
       
        
class DeleteBookView(LoginRequiredMixin, View):
    def get(self, request,id):
        try:
            book = Books.objects.get(id=id)
        except Books.DoesNotExist:
            return redirect('/show_book')
        book.delete()
        return redirect('/show_book')