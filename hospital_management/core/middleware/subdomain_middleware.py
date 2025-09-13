from django.conf import settings

class SubdomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.subdomain_urlconfs = {
            "admin": "hospital_management.subdomain_urls.admin",
            "doctor": "hospital_management.subdomain_urls.doctor",
            "nurse": "hospital_management.subdomain_urls.nurse",
            "records": "hospital_management.subdomain_urls.records",
            "pharmacy": "hospital_management.subdomain_urls.pharmacy",
            "lab": "hospital_management.subdomain_urls.lab",
            "cashier": "hospital_management.subdomain_urls.cashier",
        }

    def __call__(self, request):
        host = request.get_host().split(":")[0]

        # Check for subdomain
        parts = host.split('.')
        # This logic handles 'lvh.me' and 'hospital.com' by not matching
        if len(parts) > 2 and parts[0] in self.subdomain_urlconfs:
            subdomain = parts[0]
            request.urlconf = self.subdomain_urlconfs[subdomain]
        # Otherwise, Django will use the default ROOT_URLCONF. No need to set it.

        response = self.get_response(request)
        return response
