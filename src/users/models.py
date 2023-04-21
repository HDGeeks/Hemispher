from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.
class CreationTimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("username", email)
        return self.create_user(email, password, **extra_fields)


class ExtendedUser(AbstractUser, CreationTimeStamp):
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=255, verbose_name="email", unique=True)
    email_verified = models.BooleanField(default=False)
    middle_name = models.CharField(max_length=255)
    role = models.ForeignKey("Role", on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} {self.role}"


class Role(models.Model):
    ROLE_CHOICES = (("Admin", "Admin"), ("Data-Collector", "Data-Collector"))

    role = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.role
