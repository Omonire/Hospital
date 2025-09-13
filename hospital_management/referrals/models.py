from django.db import models
from django.conf import settings

class Referral(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
    )

    patient = models.ForeignKey("patients.Patient", on_delete=models.CASCADE, related_name="referrals")
    from_doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_referrals",
        limit_choices_to={"role": "doctor"},
    )
    to_department = models.ForeignKey(
        "departments.Department", on_delete=models.CASCADE, related_name="received_referrals"
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Referral for {self.patient.name} to {self.to_department.name}"
