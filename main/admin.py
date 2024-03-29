from django.contrib import admin
from .models import Patient,Doctor,Department
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display=('full_name','mobile_no','detail')
admin.site.register(Patient,PatientAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display=('name',)
admin.site.register(Department,DepartmentAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_display=('full_name','mobile_no')
admin.site.register(Doctor,DoctorAdmin)
