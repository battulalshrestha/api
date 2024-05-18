from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework import status
from .serializers import StudentSerializer
from .models import Student
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def studentapi(request,pk = None):
    if request.method == "GET":
        id = pk
       # print(id)
        if id is not None:
            id_student = Student.objects.get(id=id)
           # print(id_student)
            serializer = StudentSerializer(id_student)
           # print(serializer.data)
            return Response(serializer.data)
        
        id_student = Student.objects.all()
       # print(id_student)
        serializer =StudentSerializer(id_student,many =True)
       # print(serializer.data)
        # Response convert the data into json format
        return Response(serializer.data)
# Create your views here

    if request.method == "POST":
       # print(request.method)
        serializer = StudentSerializer(data = request.data)
      #  print(serializer)

        if serializer.is_valid():
            serializer.save()

            return Response({'message':'Data is being created'},status=status.HTTP_201_CREATED)
       # print(Response)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    #print(Response)
    if request.method == "PUT":
        id = pk
        id_student = Student.objects.get(pk= id)
        serializer = StudentSerializer(id_student,data=request.data)
        if serializer.is_valid():
         serializer.save()
         return Response({'msg':'message sabbai completely updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == "PATCH":
        id = pk
        id_student - Student.objects.get(pk = id)
        serializer = StudentSerializer(id_student,data=request.data,partially = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'message partialy updated'})
        return Response(serializer.errors)
    if request.method == "DELETE":
        id=pk
        id_student = Student.objects.get(pk= id)
        id_student.delete()
        return Response({'message':"The data has been deleted"})
  
  