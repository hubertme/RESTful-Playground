# Used to convert model to JSON object
from rest_framework import serializers
from . models import Employee as employee

class serializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = ('employee_id', 'firstName', 'lastName')

        # fields = '__all__' # To return all fields