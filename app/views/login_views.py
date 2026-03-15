from django.views.generic.base import TemplateView
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy

# Models
from app.models.assinatura_models import Assinatura
from app.models.treino_models import Treino

# Autenticar
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Forms
from app.forms.user_forms import UserCreationForm, UserPasswordUpdateForm, UserNameUpdateForm

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        assinatura = Assinatura.objects.get(cliente=self.request.user)
        context["treinos"] = Treino.objects.filter(cliente=self.request.user)
        context["assinatura"] = assinatura
        context["pagamentos"] = assinatura.get_all_pagamentos
        return context

class LoginView(View):
    template_name = "login/login.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(username=email, password=password)
        
        if (user):
            login(request, user)
            return redirect("user-data")
        else:
            print(user)
            return redirect("login")

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("login")

class DataUserView(LoginRequiredMixin, View):
    template_name = "authenticaded_page.html"
    login_url = "/login/"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class CreateUserView(View):
    template_name = "login/register.html"
    
    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, self.template_name, {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect("login")
        return render(request, self.template_name, {"form": form})   

class UserNameUpdateView(LoginRequiredMixin, View):
    template_name = "login/update-profile.html"

    def get(self, request, *args, **kwargs):
        form = UserNameUpdateForm(instance=request.user)
        return render(request, self.template_name, {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = UserNameUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, "Nome atualizado com sucesso")
            return redirect("user-data")

        return render(request, self.template_name, {"form": form})
    
class UserPasswordUpdateView(LoginRequiredMixin, View):
    template_name = "login/update-password.html"

    def get(self, request, *args, **kwargs):
        form = UserPasswordUpdateForm(instance=request.user)
        return render(request, self.template_name, {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = UserPasswordUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Senha atualizada com sucesso")
            return redirect("user-data")

        return render(request, self.template_name, {"form": form})
