from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from core.decorators import admin_required, doctor_required, nurse_required
from django.contrib.auth import logout as auth_logout

class CustomLoginView(LoginView):
    template_name = "users/login.html"

    def get_success_url(self):
        user = self.request.user
        # Determine the domain based on the request host
        host = self.request.get_host()
        # Use lvh.me for local development to simulate subdomains
        domain = "lvh.me:8000" if "lvh.me" in host else "hospital.com"

        subdomain = user.role

        # Construct the full URL for redirection
        # Ensure the scheme is included, especially for production
        scheme = self.request.scheme
        return f"{scheme}://{subdomain}.{domain}/"

def logout_view(request):
    auth_logout(request)
    host = request.get_host()
    domain = "lvh.me:8000" if "lvh.me" in host else "hospital.com"
    scheme = request.scheme
    return redirect(f"{scheme}://{domain}/login/")


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
