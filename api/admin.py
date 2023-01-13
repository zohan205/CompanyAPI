from django.contrib import admin
from .models import *

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','location','type')
    #search_fields = ('name')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','email','company')
    #list_display = ('company')


admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
