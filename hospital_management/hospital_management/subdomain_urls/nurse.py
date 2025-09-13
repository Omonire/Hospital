from django.urls import path
from users.views import nurse_dashboard

urlpatterns = [
    path("", nurse_dashboard, name="nurse_dashboard"),
]
