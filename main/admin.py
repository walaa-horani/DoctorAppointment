from django.contrib import admin
from .models import Patient
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display=('full_name','mobile_no','detail')
admin.site.register(Patient,PatientAdmin)