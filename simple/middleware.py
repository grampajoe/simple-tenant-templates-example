from django.conf import settings


class TenantMiddleware(object):
    def process_request(self, request):
        tenant_slug = request.GET.get('tenant', 'default')

        if tenant_slug in settings.TENANTS:
            request.tenant_slug = tenant_slug
