from django.shortcuts import render, redirect,get_object_or_404
from .models import Patient,Doctor,Department
from .forms import PatientForm,DoctorForm
from django. contrib import messages
import time
from django.core.mail import send_mail
from django.db.models import Q

# Create your views here.
def home(request):
    data = Patient.objects.all()
    departmens = Department.objects.all()
    if "q" in request.GET:
        q = request.GET['q']
        data = Patient.objects.filter(Q(full_name__icontains=q) | Q(mobile_no__icontains=q))


   
    departments = Department.objects.all()
    doctors = Doctor.objects.all()

    # Filter doctors based on selected department
     

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "patient has been added.")
            time.sleep(1)
            return redirect('home')  
    else:
        form = PatientForm()
    
    return render(request,'home.html',{'data':data, 'form': form,'departments': departments, 'doctors': doctors})

def doctor_list(request):
    departments = Department.objects.all()
    doctors = Doctor.objects.all()

    # Filter doctors based on selected department
    department_id = request.GET.get('department')
    if department_id:
        doctors = doctors.filter(department_id=department_id)

    return render(request, 'doctor_list.html', {'departments': departments, 'doctors': doctors})


def all_patients(request):
    data = Patient.objects.all()
    if "q" in request.GET:
        q = request.GET['q']
        data = Patient.objects.filter(Q(full_name__icontains=q) | Q(mobile_no__icontains=q))

       
    return render(request,'all_patients.html',{'data':data, })





def doctors(request):
    data = Doctor.objects.all()
    if "q" in request.GET:
        q = request.GET['q']
        data = Patient.objects.filter(Q(full_name__icontains=q) | Q(mobile_no__icontains=q))

       
    return render(request,'doctors.html',{'data':data, })

def about(request):
    
   

       
    return render(request,'about.html')


def service(request):
    
       
    return render(request,'service.html',)        



def testimonial(request):
    
       
    return render(request,'testimonial.html',)  


# def appointment(request):
    
       
#     return render(request,'appointment.html',)      

def contact(request):
    
       
    return render(request,'contact.html',) 

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "patient has been added.")
            # time.sleep(1)
            return redirect('add_patient')  
    else:
        form = PatientForm()
    return render(request, 'add_patient.html', {'form': form})



def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "doctor has been added.")
           
            return redirect('add_doctor')  
    else:
        form = DoctorForm()
    return render(request, 'add_doctor.html', {'form': form})


def update_doctor(request,id):
    doctor = Doctor.objects.get(id=id)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)  # Pass the instance to the form

        if form.is_valid():
            form.save()
            messages.success(request, "doctor form has been updated.")
            time.sleep(1)
            return redirect('home')  
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'update_doctor.html', {'form': form})



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