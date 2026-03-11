from django import forms
from app.models import Assinatura

class AssinaturaCreateForm(forms.ModelForm):
    class Meta:
        model = Assinatura
        fields = ["valor"]

class AssinaturaAdminCreateForm(forms.ModelForm):
    class Meta:
        model = Assinatura
        fields = ["valor", "cliente"]
    
class AssinaturaUpdateForm(forms.ModelForm):
    class Meta:
        model = Assinatura
        fields = ["valor", "status"]
