from django.shortcuts import render
# from rest_framework.generics import ListCreateAPIView
from .models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer


# from rest_framework.filters import SearchFilter
from rest_framework import filters


# class StudentList(ListCreateAPIView):

#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     filter_backends = [filters.OrderingFilter]
#     ordering_fields = ['name', 'city']

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'city']