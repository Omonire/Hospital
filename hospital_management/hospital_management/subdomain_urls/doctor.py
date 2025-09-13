from django.urls import path
from users.views import doctor_dashboard
from referrals.views import create_referral

urlpatterns = [
    path("", doctor_dashboard, name="doctor_dashboard"),
    path("referrals/create/", create_referral, name="create_referral"),
]
