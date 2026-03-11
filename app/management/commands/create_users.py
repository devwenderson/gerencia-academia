from django.core.management.base import BaseCommand
from django.core.management import call_command
from app.models.user_models import User
from app.models.assinatura_models import Assinatura, Plano
from app.management.commands.users_data import users 

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.exibir_mensagem("Criando migrações...")
        call_command("makemigrations")
        self.exibir_mensagem("Atualizando tabelas do banco de dados...")
        call_command("migrate")
        self.exibir_mensagem("Cadastrando usuários...")

        for data in users:
            if (self.verifica_usuario(data)):
                self.stdout.write(f"Usuário [{data['email']}] já existe!")
                continue

            user = User.objects.create(
                email=data['email'], 
                name=data['name'],
                is_superuser=data['is_superuser'],
                is_staff=data['is_staff'],
                is_active=True
            )
            user.set_password(data['password'])
            user.save()
        
        self.exibir_mensagem("Usuários cadastrados!")
        
        
    def verifica_usuario(self, data):
        return User.objects.filter(email=data["email"]).exists()
    
    def exibir_mensagem(self, texto):      
        self.stdout.write(f"\n**** {texto} ****\n")
        