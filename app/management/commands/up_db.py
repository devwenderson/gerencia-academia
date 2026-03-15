from django.core.management.base import BaseCommand
from django.core.management import call_command

# USERS
from app.models.user_models import User
from app.management.commands.users_data import users 

# PLANO
from app.models.assinatura_models import Plano
from decimal import Decimal

# TREINO
from app.models.treino_models import TipoTreino

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.exibir_mensagem("Criando migrações...")
        call_command("makemigrations")
        self.exibir_mensagem("Migrações feitas!")
        self.exibir_mensagem("Atualizando tabelas do banco de dados...")
        call_command("migrate")
        self.exibir_mensagem("Tabelas atualizadas!")
        
        self.create_plano()
        self.create_user()
        self.create_tipos_treinos()

    def verifica_usuario(self, data):
        return User.objects.filter(email=data["email"]).exists()

    def exibir_mensagem(self, texto):
        self.stdout.write(f"\n**** [{texto}] ****\n")

    def create_user(self):
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

    def create_plano(self):
        self.exibir_mensagem("Cadastrando plano no sistema...")
        
        Plano.objects.create(
            valor=Decimal("50.00")
        )

        self.exibir_mensagem("Plano cadastrado!")
    
    def create_tipos_treinos(self):
        self.exibir_mensagem("Cadastrando tipos dos treinos sistema...")
        tipos_treino = ["Pernas", "Peito", "Glúteos", "Ombros", "Bíceps", "Costas"]
        for tipo in tipos_treino:
            TipoTreino.objects.create(nome=tipo)
        self.exibir_mensagem("Tipos dos treinos cadastrados!")
