
from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViewSet,EmployeeViewSet

## Step 5
# Step 5.1  create router & register viewset
from rest_framework import routers
routers =routers.DefaultRouter()
routers.register(r'company',CompanyViewSet)
routers.register(r'employee',EmployeeViewSet)
urlpatterns = [
  path('',include(routers.urls))

]
