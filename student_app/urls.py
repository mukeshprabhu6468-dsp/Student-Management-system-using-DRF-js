from django.urls import path,include
from .views import *

urlpatterns = [
    path('students/',AllStudents.as_view()),
    path('students/add/',AddStudent.as_view()),
    path('students/edit/<int:pk>/',StudentEdit.as_view()),
    path('students/delete/<int:pk>/',StudentDelete.as_view()),
    path('students/<int:pk>/', StudentDetail.as_view()),
]