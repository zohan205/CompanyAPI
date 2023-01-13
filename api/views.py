from django.shortcuts import render
from rest_framework import viewsets, status
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['GET'])
    def employees(self,request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            print('This is triggered')
            emps_serializer = EmployeeSerializer(emps, many=True, context={'request':request})
            return Response(emps_serializer.data)
        except:
            return Response({
                'message': "Company might not exists!! Error"
            },status=status.HTTP_404_NOT_FOUND)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

