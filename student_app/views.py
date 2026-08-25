from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from .models import Student

from rest_framework.permissions import IsAuthenticated


class AddStudent(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AllStudents(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class StudentEdit(APIView):
    permission_classes = [IsAuthenticated]
    def put(self,request,pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({"error":"Student not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class StudentDelete(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self,request,pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({"error":"Student not found"},status=status.HTTP_404_NOT_FOUND)
        student.delete()
        return Response({"message":"Student deleted successfully"},status=status.HTTP_200_OK)

class StudentDetail(APIView):

    def get(self, request, pk):

        try:
            student = Student.objects.get(pk=pk)

        except Student.DoesNotExist:
            return Response(
                {"error": "Student Not Found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = StudentSerializer(student)

        return Response(serializer.data)