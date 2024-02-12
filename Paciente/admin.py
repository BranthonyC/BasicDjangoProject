from django.contrib import admin

# Register your models here.
from .models import Paciente, Doctor, MedicalApointment

admin.site.register(Paciente, list_display=['cui', 'name', 'age', 'email', 'phone', 'address', 'city', 'state', 'zipcode', 'country'])
admin.site.register(Doctor, list_display=['cui', 'name', 'age', 'email', 'phone', 'address', 'city', 'state', 'zipcode', 'country'])
admin.site.register(MedicalApointment, list_display=['cui', 'doctor', 'date', 'hour', 'reason', 'status'])

