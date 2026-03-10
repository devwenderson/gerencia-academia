from django.db import models
from app.models.user_models import User
from django.urls import reverse

class Treino(models.Model):
    tipo = models.CharField(verbose_name="Tipo do treino", max_length=30, blank=False, null=False)
    exercicio = models.CharField(verbose_name="Exercício", max_length=50, blank=False, null=False)
    series = models.IntegerField(verbose_name="Séries", null=False, blank=False)
    repeticoes = models.IntegerField(verbose_name="Número de repetições", null=False, blank=False)
    cliente = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Treino"
        verbose_name_plural = "Treinos"

    def __str__(self):
        return f"{self.cliente.get_short_name()}-{self.tipo}|{self.exercicio}"
    
    def get_absolute_url(self):
        return reverse("detail-treino", kwargs={"pk": self.pk})
    
