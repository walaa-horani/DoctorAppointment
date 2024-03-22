from django.urls import path
from . import views
urlpatterns=[
path('',views.home, name ='home'),
path('add_patient',views.add_patient, name ='add_patient'),
path('update_patient/<int:id>',views.update_patient, name ='update_patient'),

path('delete_patient/<int:id>',views.delete_patient, name ='delete_patient'),
path('sendEmail/<int:id>',views.sendEmail, name ='sendEmail'),

]