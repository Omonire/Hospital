from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from referrals.models import Referral

@login_required
def department_dashboard(request):
    department = request.user.department
    referrals = []
    if department:
        referrals = Referral.objects.filter(to_department=department).order_by('-created_at')

    context = {
        'referrals': referrals
    }
    return render(request, "departments/department_dashboard.html", context)
