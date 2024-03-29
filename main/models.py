from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    full_name = models.CharField(max_length=100)

    email = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class Patient(models.Model):
    full_name = models.CharField(max_length=100)

    email = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=100)
    address = models.TextField()
    detail = models.TextField()
    visit_date = models.DateTimeField(auto_now_add=True)
    next_visit_date = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name