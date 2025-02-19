# app1/serializers.py
from rest_framework import serializers
from .models import Student, LibraryRegister

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class LibraryRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryRegister
        fields = '__all__'