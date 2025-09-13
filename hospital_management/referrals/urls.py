from django.urls import path
from .views import create_referral, update_referral_status

app_name = 'referrals'

urlpatterns = [
    path('create/', create_referral, name='create_referral'),
    path('<int:referral_id>/update_status/', update_referral_status, name='update_referral_status'),
]
