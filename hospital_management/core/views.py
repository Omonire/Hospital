from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def placeholder_view(request):
    return HttpResponse(f"<h1>Dashboard for {request.user.role}</h1><p>Welcome, {request.user.username}</p>")
