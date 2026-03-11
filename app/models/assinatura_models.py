from django.db import models
from app.models.pagamento_models import Pagamento
from django.urls import reverse
from datetime import timedelta

class AssinaturaStatus(models.IntegerChoices):
    ATIVADO = 1, "Ativado"
    DESATIVADO = 2, "Desativado"

class Assinatura(models.Model):
    cliente = models.OneToOneField("app.User", on_delete=models.PROTECT, verbose_name="Cliente")
    valor = models.DecimalField(verbose_name="Valor", max_digits=6, decimal_places=2, blank=False, null=False)
    criado_em = models.DateField(verbose_name="Criado em", auto_now_add=True, blank=True, null=False)
    desativado_em = models.DateField(verbose_name="Desativado em", auto_now=False, blank=True, null=True)
    status = models.IntegerField(verbose_name="Status", choices=AssinaturaStatus, default=AssinaturaStatus.ATIVADO)

    class Meta:
        verbose_name = "Assinatura"
        verbose_name_plural = "Assinaturas"

    def __str__(self):
        return f"{self.cliente.get_full_name()} | {self.status}"
    
    def get_absolute_url(self):
        return reverse("detail-assinatura", kwargs={"pk": self.pk})
    
    def save(self, **kwargs):
        super().save(**kwargs)
        vencimento = self.criado_em + timedelta(days=30)
        Pagamento.objects.create(
            assinatura=self,
            valor=self.valor,
            vencimento=vencimento
        )
    
class Plano(models.Model):
    valor = models.DecimalField(verbose_name="Valor do plano", max_digits=6, decimal_places=2, null=False)
    
