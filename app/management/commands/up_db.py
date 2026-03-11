from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.exibir_mensagem("Criando migrações...")
        call_command("makemigrations")
        self.exibir_mensagem("Atualizando tabelas do banco de dados...")
        call_command("migrate")
    
    def exibir_mensagem(self, texto):
        self.stdout.write(f"\n**** {texto} ****\n")
        