from rest_framework import serializers
from api.models import Company
from api.models import Employee

# Create serializers here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields= "__all__" ## Include one field or multiple field 


## Employee Serializer

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Employee
        fields="__all__" ## We can pass as list 