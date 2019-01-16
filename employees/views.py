from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Employee as employee, News as news
from . serializers import EmployeeSerializer, NewsSerializer

# Create your views here.
class employeeView(APIView):

    def get(self, request):
        employees = employee.objects.all()
        viewSerializer = EmployeeSerializer(employees, many=True)
        return Response(viewSerializer.data)

    def post(self, request):
        viewSerializer = EmployeeSerializer(data=request.data)
        if viewSerializer.is_valid():
            viewSerializer.save()

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

    def put(self, request):
        pass

class newsView(APIView):

    def get(self, request):
        newsInView = news.objects.all()
        viewSerializer = NewsSerializer(newsInView, many=True)
        return Response(viewSerializer.data)

    def post(self, request):
        viewSerializer = NewsSerializer(data=request.data)
        if viewSerializer.is_valid():
            viewSerializer.save()

            news_title = viewSerializer.data.get('news_title')
            employee_id = viewSerializer.data.get('employee_id')
            date_created = viewSerializer.data.get('date_created')
            return Response({
                "news_title": news_title,
                "employee_id": employee_id,
                "date_created": date_created,
            })
        else:
            return Response(viewSerializer.errors, status=status.HTTP_400_BAD_REQUEST)