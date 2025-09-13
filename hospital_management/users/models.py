from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("doctor", "Doctor"),
        ("nurse", "Nurse"),
        ("records", "Records"),
        ("pharmacy", "Pharmacy"),
        ("lab", "Lab"),
        ("cashier", "Cashier"),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    department = models.ForeignKey(
        "departments.Department", on_delete=models.SET_NULL, null=True, blank=True
    )
    created_by = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.username
