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
        viewSerializer = serializer(data=request.data)
        if viewSerializer.is_valid():
            employee_id = viewSerializer.data.get('employee_id')
            first_name = viewSerializer.data.get('first_name')
            last_name = viewSerializer.data.get('last_name')
            date_created = viewSerializer.data.get('date_created')
            return Response({"employee_id": employee_id,
                             "first_name": first_name,
                             "last_name": last_name,
                             "date_created": date_created})
        else:
            return Response(viewSerializer.errors, status=status.HTTP_400_BAD_REQUEST)