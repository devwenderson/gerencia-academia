from django import forms
from app.models import Treino

class TreinoCreateForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = "__all__"