from django.contrib import admin
from .models import Student, LibraryRegister

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'class_name', 'age', 'rollno', 'fees_paid', 'created_at', 'active')
    search_fields = ('name', 'rollno')
    list_filter = ('class_name', 'fees_paid', 'active')
    
    
@admin.register(LibraryRegister)
class LibraryRegisterAdmin(admin.ModelAdmin):
    list_display = ('slno', 'name', 'author', 'created_at', 'active')
    search_fields = ('name', 'author')
    list_filter = ('active',)