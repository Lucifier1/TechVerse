from django.shortcuts import redirect
from django.urls import reverse

class AdminAccessRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path

        # Allow normal users to access anything except adminapp URLs
        if 'adminapp' in path:
            if not request.user.is_authenticated or not request.user.is_staff:
                return redirect(reverse('admin_login'))  # 👈 make sure this name exists in your URLConf

        return self.get_response(request)
