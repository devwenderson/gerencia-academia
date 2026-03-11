from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone
from app.models.assinatura_models import Assinatura, Plano

class CustomUserManager(UserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email inválido")

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields 
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(
            email=email,
            password=password
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="Email", blank=True, default='', unique=True)
    name = models.CharField(verbose_name="Nome", max_length=255, blank=True, default='')

    is_active = models.BooleanField(verbose_name="Ativo", default=True)
    is_superuser = models.BooleanField(verbose_name="Administrador", default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(verbose_name="Cadastrado em", default=timezone.now)
    last_login = models.DateTimeField(verbose_name="Ultimo login", blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
    
    def __str__(self):
        return f"{self.email}"

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name or self.email.split("@")[0]
    
    def save(self, **kwargs):
        super().save(**kwargs)

        if (self.is_superuser):
            return

        # Se existir uma assinatura cadastrada
        is_assinatura_cliente = Assinatura.objects.filter(cliente=self)
        if not (is_assinatura_cliente):
            plano = Plano.objects.first()
            Assinatura.objects.create(cliente=self, valor=plano.valor)
        
        
