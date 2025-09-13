from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.decorators import doctor_required
from .forms import ReferralForm
from .models import Referral
from django.urls import reverse

@login_required
@doctor_required
def create_referral(request):
    if request.method == 'POST':
        form = ReferralForm(request.POST)
        if form.is_valid():
            referral = form.save(commit=False)
            referral.from_doctor = request.user
            referral.save()
            return redirect('doctor_dashboard') # Or a success page
    else:
        form = ReferralForm()
    return render(request, 'referrals/create_referral.html', {'form': form})

@login_required
def update_referral_status(request, referral_id):
    referral = get_object_or_404(Referral, id=referral_id)

    # Security check: ensure the user belongs to the department
    # the referral was sent to.
    if request.user.department != referral.to_department:
        from django.core.exceptions import PermissionDenied
        raise PermissionDenied

    if request.method == 'POST':
        status = request.POST.get('status')
        if status in ['pending', 'in_progress', 'done']:
            referral.status = status
            referral.save()

    # Redirect back to the user's dashboard based on their role
    role_dashboard_map = {
        'records': 'records_dashboard',
        'pharmacy': 'pharmacy_dashboard',
        'lab': 'lab_dashboard',
        'cashier': 'cashier_dashboard',
    }
    dashboard_url_name = role_dashboard_map.get(request.user.role)

    # To redirect to a subdomain, we need to construct the full URL
    host = request.get_host()
    domain = "lvh.me:8000" if "lvh.me" in host else "hospital.com"
    subdomain = request.user.role
    scheme = request.scheme
    return redirect(f"{scheme}://{subdomain}.{domain}/")
