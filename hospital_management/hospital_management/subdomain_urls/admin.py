from django.urls import path
from users.views import admin_dashboard

urlpatterns = [
    path("", admin_dashboard, name="admin_dashboard"),
]
