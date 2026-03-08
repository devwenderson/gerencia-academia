from django.views.generic.base import TemplateView
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages

# Models
from app.models.user import User

# Autenticar
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


# Forms
from app.forms.user import UserCreationForm, UserUpdateForm

class HomePageView(TemplateView):
    template_name = "index.html"

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

class UpdateUserView(LoginRequiredMixin, View):
    template_name = "login/update-profile.html"

    def get(self, request, *args, **kwargs):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Perfil atualizado com sucesso")
            return redirect("user-data")

        return render(request, self.template_name, {"form": form})
