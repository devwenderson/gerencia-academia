from django.core.management.base import BaseCommand
from django.core.management import call_command

# Models
from app.models.assinatura_models import Plano

# Ultil
from decimal import Decimal

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.exibir_mensagem("Criando migrações...")
        call_command("makemigrations")
        self.exibir_mensagem("Atualizando tabelas do banco de dados...")
        call_command("migrate")
        self.exibir_mensagem("Cadastrando plano no sistema...")
        
        Plano.objects.create(
            valor=Decimal("50.00")
        )

        self.exibir_mensagem("Plano cadastrado!")
    
    def exibir_mensagem(self, texto):
        self.stdout.write(f"\n**** {texto} ****\n")
        