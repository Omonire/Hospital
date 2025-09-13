from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

def role_required(role):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                # This will be handled by login_required decorator if used,
                # but as a safeguard.
                from django.contrib.auth.views import redirect_to_login
                return redirect_to_login(request.get_full_path())

            if request.user.role != role:
                raise PermissionDenied
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

def admin_required(view_func):
    return role_required('admin')(view_func)

def doctor_required(view_func):
    return role_required('doctor')(view_func)

def nurse_required(view_func):
    return role_required('nurse')(view_func)

def records_required(view_func):
    return role_required('records')(view_func)

def pharmacy_required(view_func):
    return role_required('pharmacy')(view_func)

def lab_required(view_func):
    return role_required('lab')(view_func)

def cashier_required(view_func):
    return role_required('cashier')(view_func)
