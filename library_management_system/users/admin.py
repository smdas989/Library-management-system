from django.contrib import admin
from .models import User,Student,Librarian,Admin, Department,Role,Faculty
# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Librarian)
admin.site.register(Admin)
admin.site.register(Department)
admin.site.register(Role)
