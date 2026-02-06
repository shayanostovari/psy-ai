from django.conf import settings
from django.http import HttpResponseForbidden

class WebhookAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/api/analyze/"):
            secret = request.headers.get("X-WP-SECRET")
            if secret != settings.WP_SECRET:
                return HttpResponseForbidden("Forbidden")
        return self.get_response(request)
