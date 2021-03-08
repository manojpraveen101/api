from rest_framework import serializers
from crudapi.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id',
                  'firstname',
                  'lastname')

