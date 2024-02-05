from django.contrib import admin
from .models import Questions, Appointments, Prescription
from .models import Responses
# Register your models here.
admin.site.register(Questions)
admin.site.register(Responses)
admin.site.register(Appointments)
admin.site.register(Prescription)