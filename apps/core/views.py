from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

from apps.core.forms import ApplicationForm
from apps.core.models import Application


class Home(TemplateView):
    template_name = 'home.html'


class RegisterView(CreateView):
    template_name = 'register.html'
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Вы успешно зарегистрированы')
        return response


class ApplicationViews(LoginRequiredMixin, CreateView):
    template_name = 'application.html'
    model = Application
    form_class = ApplicationForm
    success_url = reverse_lazy('application')

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Данные успешно отправлены')
        return response


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect(reverse_lazy('home'))
