from django.db import models
import datetime 
from users.models import User, Librarian

class Books(models.Model):
    GENRE = (
        ('Motivational', 'Motivational'),
        ('Govt_exam', 'Govt_exam'),
        ('Engineering', 'Engineering'),
        ('Science_and_Tech', 'Science_and_Tech'),
        ('Novels', 'Novels'),
        ('Biographies','Biographies')
    )
    
    title = models.CharField(max_length=255,blank=True, null=True)
    author = models.CharField(max_length=255,blank=True, null=True)
    no_of_copies = models.BigIntegerField(blank=True, null=True)
    no_of_available_copies = models.BigIntegerField(blank=True, null=True)
    genre = models.CharField(max_length=255, choices=GENRE, blank=True, null=True)
    book_image = models.ImageField(upload_to ='media/books/', blank=True, null=True) 

    def __str__(self):
        return self.title

class BookRecord(models.Model):
    borrower_name = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE, blank=True, null=True)
    issue_date = models.DateField(auto_now_add=True,blank=True, null=True)
    due_date = models.DateField(default=None, blank=True,null=True)
    return_date = models.DateField(default=None, blank=True,null=True)
  
    def __str__(self):
        return self.book.title

    def save(self, *args, **kwargs):
        from datetime import datetime, timedelta
        self.due_date = datetime.now() + timedelta(days=10)
        super(BookRecord, self).save(*args, **kwargs)
