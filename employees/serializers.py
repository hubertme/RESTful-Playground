# Used to convert model to JSON object
from rest_framework import serializers
from . models import Employee as employee, News as news

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = ('employee_id', 'first_name', 'last_name', 'date_created')

        # fields = '__all__' # To return all fields


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = news
        fields = '__all__'