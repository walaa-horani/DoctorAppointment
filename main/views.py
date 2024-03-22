from django.shortcuts import render, redirect,get_object_or_404
from .models import Patient
from .forms import PatientForm
from django. contrib import messages
import time
from django.core.mail import send_mail
from django.db.models import Q

# Create your views here.
def home(request):
    data = Patient.objects.all()
    if "q" in request.GET:
        q = request.GET['q']
        data = Patient.objects.filter(Q(full_name__icontains=q) | Q(mobile_no__icontains=q))

    
    return render(request,'home.html',{'data':data})


def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "patient has been added.")
            time.sleep(1)
            return redirect('home')  
    else:
        form = PatientForm()
    return render(request, 'add_patient.html', {'form': form})


def update_patient(request,id):
    patient = Patient.objects.get(id=id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)  # Pass the instance to the form

        if form.is_valid():
            form.save()
            messages.success(request, "patient form has been updated.")
            time.sleep(1)
            return redirect('home')  
    else:
        form = PatientForm(instance=patient)
    return render(request, 'update_patient.html', {'form': form})



def delete_patient(request, id):
    patient = Patient.objects.filter(id=id).delete()
    
    
        
    messages.success(request, "Patient has been deleted successfully.")
    return redirect('home')
    


def sendEmail(request,id):
    patient = Patient.objects.get(id=id)
    send_mail(
    "next visit reminder",
    "your next visit is on"+ str(patient.next_visit_date) ,
    "clinic@example.com",
    [patient.email],
    fail_silently=False,
)
    messages.success(request, "Email has been sent.")

    return redirect('/')