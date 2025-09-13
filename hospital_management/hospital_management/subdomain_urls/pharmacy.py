from django.urls import path, include
from departments.views import department_dashboard

urlpatterns = [
    path("", department_dashboard, name="pharmacy_dashboard"),
    path("referrals/", include("referrals.urls", namespace="referrals")),
]
