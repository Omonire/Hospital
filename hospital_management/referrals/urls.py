from django.urls import path
from .views import update_referral_status

app_name = 'referrals'

urlpatterns = [
    path("<int:referral_id>/update_status/", update_referral_status, name="update_referral_status"),
]
