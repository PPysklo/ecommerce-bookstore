from django.shortcuts import redirect
from django.urls import reverse

class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin'):
            if not request.user.is_authenticated:
                return redirect(reverse('app_users:login-register'))
            if not request.user.is_superuser and not request.user.groups.filter(name='Order Manager').exists():
                return redirect(reverse('app_books:books-list'))
        response = self.get_response(request)
        return response