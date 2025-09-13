from django.db import models
from django.conf import settings

class Patient(models.Model):
    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    )

    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    contact_info = models.CharField(max_length=255)
    medical_history = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_patients"
    )

    def __str__(self):
        return self.name

class NurseTask(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
    )

    nurse = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="nurse_tasks",
        limit_choices_to={"role": "nurse"},
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="nurse_tasks")
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    assigned_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="assigned_nurse_tasks",
        limit_choices_to={"role": "doctor"},
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Task for {self.patient.name} by {self.nurse.username}"
