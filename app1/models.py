from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)
    age = models.IntegerField()
    rollno = models.CharField(max_length=20, unique=True)
    fees_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class LibraryRegister(models.Model):
    slno = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name