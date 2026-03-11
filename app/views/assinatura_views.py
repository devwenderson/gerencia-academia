from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from app.models.assinatura_models import Assinatura
from app.models.pagamento_models import Pagamento

from app.forms.assinatura_forms import AssinaturaCreateForm, AssinaturaAdminCreateForm, AssinaturaUpdateForm

class AssinaturaCreateView(LoginRequiredMixin, CreateView):
    template_name = "assinaturas/create.html"
    model = Assinatura
    success_url = reverse_lazy("list-assinatura")

    def get_form_class(self):
        if not self.request.user.is_staff:
            return AssinaturaCreateForm
        else:
            return AssinaturaAdminCreateForm

    def form_valid(self, form):
        if not self.request.user.is_staff:
            form.instance.cliente = self.request.user
      
        response = super().form_valid(form)

        assinatura = self.object
        vencimento = assinatura.criado_em + timedelta(days=30)

        pagamento = Pagamento.objects.create(
            assinatura=assinatura,
            valor=assinatura.valor,
            vencimento=vencimento
        )

        messages.success(self.request, "Assinatura criada com sucesso")

        return response

class AssinaturaDetailView(LoginRequiredMixin, DetailView):
    model = Assinatura
    template_name = "assinaturas/detail.html"
    context_object_name = "assinatura"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        assinatura = self.object
        pagamentos = Pagamento.objects.filter(assinatura=assinatura)
        context["pagamentos"] = pagamentos

        return context

class AssinaturaUpdateView(LoginRequiredMixin, UpdateView):
    model = Assinatura
    template_name = "assinaturas/update.html"
    context_object_name = "assinatura"
    form_class = AssinaturaUpdateForm

class AssinaturaListView(LoginRequiredMixin, ListView):
    model = Assinatura
    context_object_name = "assinaturas"
    
    def get_queryset(self):
        if not self.request.user.is_staff:
            objetos = Assinatura.objects.filter(cliente=self.request.user)
        else:
            objetos = Assinatura.objects.all()
        return objetos
    
    def get_template_names(self):
        if not self.request.user.is_staff:
            _template_name = "assinaturas/list.html"
        else:
            _template_name = "assinaturas/admin-list.html"
        return _template_name
    
class AssinaturaDeleteView(LoginRequiredMixin, DeleteView):
    model = Assinatura
    template_name = "assinaturas/delete.html"
    context_object_name = "assinatura"
    success_url = reverse_lazy("list-assinatura")

class PagamentoListView(LoginRequiredMixin, ListView):
    model = Pagamento
    template_name = "pagamentos/admin-list.html"
    context_object_name = "pagamentos"
        