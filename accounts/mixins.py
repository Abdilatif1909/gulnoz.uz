from django.contrib.auth.mixins import AccessMixin

from .utils import is_admin, is_company, is_investor


class AdminOrCompanyRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if is_admin(request.user) or is_company(request.user):
            return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()


class InvestorRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if is_admin(request.user) or is_investor(request.user):
            return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()
