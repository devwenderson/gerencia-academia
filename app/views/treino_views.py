from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from app.models.treino_models import Treino

from app.forms.treino_forms import TreinoCreateForm, TreinoUpdateForm

class TreinoCreateView(LoginRequiredMixin, CreateView):
    model = Treino
    form_class = TreinoCreateForm
    template_name = "treinos/create.html"
    success_url = reverse_lazy("list-treino")

    def form_valid(self, form):
        if not(self.request.user.is_staff):
            form.instance.cliente = self.request.user
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        if not self.request.user.is_staff:
            form.fields.pop("cliente")
        return form
    
class TreinoListView(LoginRequiredMixin, ListView):
    model = Treino
    context_object_name = "treinos"
    template_name = "treinos/list.html"
    
    def get_queryset(self):
        if not self.request.user.is_staff:
            return Treino.objects.filter(cliente=self.request.user)
        else:
            return Treino.objects.all()
    
class TreinoUpdateView(LoginRequiredMixin, UpdateView):
    model = Treino
    template_name = "treinos/update.html"
    form_class = TreinoUpdateForm
    context_object_name = "treino"

    def form_valid(self, form):
        messages.success(self.request, "Treino atualizado com sucesso!")
        return super().form_valid(form)
    

class TreinoDetailView(LoginRequiredMixin, DetailView):
    model = Treino
    template_name = "treinos/detail.html"
    context_object_name = "treino"
    
