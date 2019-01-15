from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Employee as employee
from . serializers import serializer

# Create your views here.
class employeeView(APIView):

    def get(self, request):
        employees = employee.objects.all()
        viewSerializer = serializer(employees, many=True)
        return Response(viewSerializer.data)

    def post(self, request):
        pass