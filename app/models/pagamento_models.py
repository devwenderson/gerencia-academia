from django.db import models
from django.urls import reverse
from app.models import Assinatura

class PagamentoStatus(models.IntegerChoices):
    PENDENTE = 1, "Pendente"
    PAGO = 2, "Pago"
    ATRASADO = 3, "Atrasado"

class Pagamento(models.Model):
    assinatura = models.ForeignKey(Assinatura, on_delete=models.CASCADE, verbose_name="Assinatura")
    valor = models.DecimalField(verbose_name="Valor", max_digits=6, decimal_places=2, blank=False, null=False)
    vencimento = models.DateField(verbose_name="Vencimento em", blank=True, null=False)
    status = models.IntegerField(verbose_name="Satus", choices=PagamentoStatus, default=PagamentoStatus.PENDENTE)

    def __str__(self):
        return f"{self.status} | Vencimento em: {self.vencimento} | Pagamento de {self.assinatura.cliente.get_full_name()}"
    
    def get_absolute_url(self):
        return reverse("detail-pagamento", kwargs={"pk": self.pk})
 
    