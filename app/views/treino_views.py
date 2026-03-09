from django.views.generic import CreateView, ListView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from app.models.treino_models import Treino

from app.forms.treino_forms import TreinoCreateForm

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
        return Treino.objects.filter(cliente=self.request.user)
