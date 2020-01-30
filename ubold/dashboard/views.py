from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import TemplateView

User = get_user_model()


class DashboardView(LoginRequiredMixin, TemplateView):
    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        return context


dashboard_view = DashboardView.as_view(template_name="dashboard/default.html")
