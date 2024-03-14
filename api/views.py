from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class = CompanySerializer

    ## Custom Urls
    #company/1/employee/
    @action(detail=True,methods=['get'])

    def employee(self,request,pk=None):
        try:
            company=Company.objects.get(pk=pk) ## First get the company object based on Primary Key (pk)
            emp=Employee.objects.filter(company=company) ## Filter the  Employee data based on company object
            ## We need to pass the data into json format so we need one serializer
            emp_serializer=EmployeeSerializer(emp,many=True,context={'request':request})
            return Response(emp_serializer.data)
        except Exception as e:
            print(e)
            return Response(
                {
                    'message':'Company might not exist !! Error'
                }
            )



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    
