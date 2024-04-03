from django.urls import path
from . import views
urlpatterns=[
path('',views.home, name ='home'),
path('all_patients',views.all_patients, name ='all_patients'),
path('add_patient',views.add_patient, name ='add_patient'),
path('doctors',views.doctors, name ='doctors'),
path('add_doctor',views.add_doctor, name ='add_doctor'),
path('delete_doctor/<int:id>',views.delete_doctor, name ='delete_doctor'),
path('about',views.about, name ='about'),
path('doctor_list', views.doctor_list, name='doctor_list'),

path('service',views.service, name ='service'),

path('testimonial',views.testimonial, name ='testimonial'),



path('contact',views.contact, name ='contact'),


path('update_patient/<int:id>',views.update_patient, name ='update_patient'),
path('update_doctor/<int:id>',views.update_doctor, name ='update_doctor'),

path('delete_patient/<int:id>',views.delete_patient, name ='delete_patient'),
path('sendEmail/<int:id>',views.sendEmail, name ='sendEmail'),

]