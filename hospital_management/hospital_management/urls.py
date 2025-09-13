from django.contrib import admin
from django.urls import path, include
from users.views import CustomLoginView, logout_view, admin_dashboard, doctor_dashboard, nurse_dashboard
from departments.views import department_dashboard

urlpatterns = [
    # Admin site (using a non-standard path to avoid conflict with /admin/ dashboard)
    path('site-admin/', admin.site.urls),

    # Auth
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),

    # Role Dashboards
    path('admin/', admin_dashboard, name='admin_dashboard'),
    path('doctor/', doctor_dashboard, name='doctor_dashboard'),
    path('nurse/', nurse_dashboard, name='nurse_dashboard'),
    path('records/', department_dashboard, name='records_dashboard'),
    path('pharmacy/', department_dashboard, name='pharmacy_dashboard'),
    path('lab/', department_dashboard, name='lab_dashboard'),
    path('cashier/', department_dashboard, name='cashier_dashboard'),

    # App-specific URLs
    path('referrals/', include('referrals.urls', namespace='referrals')),
]
