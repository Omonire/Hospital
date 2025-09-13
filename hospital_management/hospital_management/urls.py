from django.contrib import admin
from django.urls import path
from users.views import CustomLoginView, logout_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
]
