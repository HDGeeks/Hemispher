from django.contrib import admin

# Register your models here.
from .models import ExtendedUser,Role


@admin.register(ExtendedUser, Role)
class PaymentAdmin(admin.ModelAdmin):
    pass