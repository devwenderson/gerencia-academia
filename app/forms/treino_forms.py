from django import forms
from app.models import Treino

class TreinoCreateForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = "__all__"

class TreinoUpdateForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = ["tipo", "exercicio", "series", "repeticoes"]