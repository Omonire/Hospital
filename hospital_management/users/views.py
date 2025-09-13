from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from core.decorators import admin_required, doctor_required, nurse_required
from django.contrib.auth import logout as auth_logout

class CustomLoginView(LoginView):
    template_name = "users/login.html"

    def get_success_url(self):
        user = self.request.user

        # Map roles to their dashboard URL names
        role_dashboard_map = {
            'admin': 'admin_dashboard',
            'doctor': 'doctor_dashboard',
            'nurse': 'nurse_dashboard',
            'records': 'records_dashboard',
            'pharmacy': 'pharmacy_dashboard',
            'lab': 'lab_dashboard',
            'cashier': 'cashier_dashboard',
        }

        # Get the URL name for the user's role, default to login page if role not found
        url_name = role_dashboard_map.get(user.role, 'login')
        return reverse(url_name)

def logout_view(request):
    auth_logout(request)
    return redirect('login')


@login_required
@admin_required
def admin_dashboard(request):
    return render(request, "users/admin_dashboard.html")

@login_required
@doctor_required
def doctor_dashboard(request):
    return render(request, "users/doctor_dashboard.html")

@login_required
@nurse_required
def nurse_dashboard(request):
    return render(request, "users/nurse_dashboard.html")
