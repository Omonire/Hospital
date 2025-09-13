from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from core.decorators import doctor_required
from .forms import ReferralForm
from .models import Referral

@login_required
@doctor_required
def create_referral(request):
    if request.method == 'POST':
        form = ReferralForm(request.POST)
        if form.is_valid():
            referral = form.save(commit=False)
            referral.from_doctor = request.user
            referral.save()
            # Redirect to the doctor dashboard after creating a referral
            return redirect('doctor_dashboard')
    else:
        form = ReferralForm()
    return render(request, 'referrals/create_referral.html', {'form': form})

@login_required
def update_referral_status(request, referral_id):
    referral = get_object_or_404(Referral, id=referral_id)

    # Security check: ensure the user belongs to the department the referral was sent to.
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

    # Get the URL name for the user's role
    dashboard_url_name = role_dashboard_map.get(request.user.role)

    if dashboard_url_name:
        return redirect(reverse(dashboard_url_name))
    else:
        # Fallback to the login page if the role has no dashboard
        return redirect(reverse('login'))
