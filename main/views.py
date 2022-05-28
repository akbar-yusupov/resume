from dateutil import relativedelta
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import DetailView, FormView, ListView

from . import forms, models
from .models import Portfolio

User = get_user_model()


class IndexView(View):
    template_name = "main/index.html"

    def get(self, request, *args, **kwargs):
        age = relativedelta.relativedelta(
            timezone.now().date(), User.objects.first().birth_date
        ).years
        work_experience = models.WorkExperience.objects.all()
        skills = models.Skills.objects.all()
        education = models.Education.objects.all()
        languages = models.Languages.objects.all()
        context = {
            "age": age,
            "work_experience": work_experience,
            "skills": skills,
            "education": education,
            "languages": languages,
        }
        return render(request, self.template_name, context)


class PortfolioListView(ListView):
    model = Portfolio
    template_name = "main/portfolio_list.html"
    context_object_name = "portfolio"

    def get_queryset(self):
        self.search = self.request.GET.get("q", None)
        if self.search:
            portfolio = get_list_or_404(
                self.model, is_active=True, technologies__pk__in=self.search
            )
            return portfolio
        else:
            return self.model.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tech_name"] = models.Skills.objects.filter(
            pk=self.search
        ).first()
        return context


class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = "main/portfolio_detail.html"
    context_object_name = "project"

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)


class ContactFormView(FormView):
    template_name = "main/contact.html"
    form_class = forms.ContactForm
    success_url = reverse_lazy("main:index")

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, _("Thank you. I will be in touch soon.")
        )
        return super().form_valid(form)
