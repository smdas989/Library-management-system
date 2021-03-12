from django.shortcuts import render, redirect
from django.views import View
from .models import Books, BookRecord
from .forms import BookAddForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
import datetime

class ShowBookView(LoginRequiredMixin, View):
    def get(self, request):
        books = Books.objects.all()
        return render(request, "allbooks.html",{'books':books})

class IssueBookView(LoginRequiredMixin, View):
    def get(self, request,id):
        book = Books.objects.get(id=id)
        book_records = BookRecord.objects.filter(Q(borrower_name=request.user) & Q(book=book))
        issued_book_flag=1
        if book_records:
            for book_record in book_records:
                if book_record.return_date is None:
                    issued_book_flag=0
                    
        issued_book_count = 0
        book_records = BookRecord.objects.filter(borrower_name=request.user)
        if book_records:
            for book_record in book_records:
                if book_record.return_date is None:
                    issued_book_count+=1
        
        if issued_book_flag == 0:
            messages.error(request,'Sorry! You have already issued this book')
            return redirect('/show_book')
        elif issued_book_count > 2:
            messages.error(request,'Sorry! You can issue maximum of three books at a time')
            return redirect('/show_book')
        elif book.no_of_available_copies < 1:
            messages.error(request,'Sorry! This book is not available')
            return redirect('/show_book')
        else:
            book_record = BookRecord(borrower_name=request.user,book=book)
            book.no_of_available_copies = book.no_of_available_copies - 1
            book_record.save()
            book.save()
            messages.success(request,'You have successfully issued this book')
            return redirect('/user_profile')

class ReturnBookView(LoginRequiredMixin, View):
    def get(self, request,id):
        book_record = BookRecord.objects.get(id=id)
        book_record.return_date = datetime.datetime.now()
        book_record.save()
        book = Books.objects.get(title=book_record.book)
        book.no_of_available_copies = book.no_of_available_copies + 1
        book.save()
        messages.success(request,'You have successfully returned this book')
        return redirect('/user_profile')

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
        return redirect(self.request.path_info)

class ShowBookDetailsView(LoginRequiredMixin, View):
    def get(self, request,id):
        book = Books.objects.get(id=id)
        return render(request, "book_details.html",{'book':book})

class IncrementDecrementCopyView(LoginRequiredMixin, View):
    def post(self, request):
        choice = request.POST.get('func')
        book_id = request.POST.get('id')
        book = Books.objects.get(id=book_id)
        success=True
        if choice == 'increment':
            success = True
            book.no_of_copies = book.no_of_copies + 1
            book.no_of_available_copies = book.no_of_available_copies + 1
            book.save()
        else:
            if book.no_of_available_copies < 1:
                if book.no_of_copies < 2:
                    success=False
                else:
                    book.no_of_copies = book.no_of_copies - 1
                    book.save()
            else:
                book.no_of_copies = book.no_of_copies - 1
                book.no_of_available_copies = book.no_of_available_copies - 1
                book.save()
        data = {
        'no_of_copies': book.no_of_copies,
        'no_of_available_copies': book.no_of_available_copies,
        }
        print(data)
        return JsonResponse(data)
