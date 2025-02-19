# app1/views.py
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student, LibraryRegister
from .serializers import StudentSerializer , LibraryRegisterSerializer # Corrected import statement
from django.http import HttpResponse

# def welcome(request):
#     return HttpResponse("Welcome to the Student & Library Management System!")
def welcome(request):
    content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
                background: url('') no-repeat center center fixed;
                background-color: black;
                background-size: cover;
                color: magenta;
                text-shadow: 2px 2px 5px rgba(128, 128, 128, 1);
            }
            h1 {
                font-size: 3rem;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to the Student & Library Management System!</h1>
    </body>
    </html>
    """
    return HttpResponse(content)

@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# class LibraryRegisterListCreateView(ListCreateAPIView):
#     queryset = LibraryRegister.objects.all()
#     serializer_class = LibraryRegisterSerializer

# class LibraryRegisterRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
#     queryset = LibraryRegister.objects.all()
#     serializer_class = LibraryRegisterSerializer
    
    
class LibraryRegisterListCreateView(APIView):
    """
    Class-based view for listing all LibraryRegister entries and creating a new entry.
    """

    def get(self, request):
        library_registers = LibraryRegister.objects.all()
        serializer = LibraryRegisterSerializer(library_registers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LibraryRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LibraryRegisterRetrieveUpdateDestroyView(APIView):
    """
    Class-based view for retrieving, updating, and deleting a specific LibraryRegister entry.
    """

    
    def get_object(self, slno):
        try:
            return LibraryRegister.objects.get(slno=slno)
        except LibraryRegister.DoesNotExist:
            return None

    # GET: Retrieve a specific LibraryRegister entry
    def get(self, request, slno):
        library_register = self.get_object(slno)
        if library_register:
            serializer = LibraryRegisterSerializer(library_register)
            return Response(serializer.data)
        return Response(
            {"error": "LibraryRegister not found"}, status=status.HTTP_404_NOT_FOUND
        )

    
    def put(self, request, slno):
        library_register = self.get_object(slno)
        if library_register:
            serializer = LibraryRegisterSerializer(library_register, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {"error": "LibraryRegister not found"}, status=status.HTTP_404_NOT_FOUND
        )

    
    def patch(self, request, slno):
        library_register = self.get_object(slno)
        if library_register:
            serializer = LibraryRegisterSerializer(
                library_register, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {"error": "LibraryRegister not found"}, status=status.HTTP_404_NOT_FOUND
        )

    def delete(self, request, slno):
        library_register = self.get_object(slno)
        if library_register:
            library_register.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"error": "LibraryRegister not found"}, status=status.HTTP_404_NOT_FOUND
        )

    
