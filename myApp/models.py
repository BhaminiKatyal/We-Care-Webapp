from django.db import models

# Create your models here.
class Questions(models.Model):
    question = models.TextField()

    def __str__(self):
        return self.question
    
    class Meta:
        db_table = "questionTable"

class Responses(models.Model):
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    
    class Meta:
        db_table = "responses"

class Appointments(models.Model):
    email = models.CharField(max_length=50)
    time = models.DateTimeField()
    doctor = models.CharField(max_length = 50)

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = "appointments"

from django.db import models

class Prescription(models.Model):
    address = models.TextField(default=None)
    file = models.FileField(upload_to='documents/django/')