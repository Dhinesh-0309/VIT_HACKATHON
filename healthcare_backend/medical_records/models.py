from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, related_name='records', on_delete=models.CASCADE)
    parent_health_history = models.TextField()
    patient_health_history = models.TextField()
    approved_doctors = models.ManyToManyField('Doctor', blank=True)
    
    def __str__(self):
        return f"Medical Record for {self.patient.first_name} {self.patient.last_name}"

class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"
