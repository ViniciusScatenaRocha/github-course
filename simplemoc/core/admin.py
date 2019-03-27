from django.contrib import admin
from .models import Pessoas, Custos, Pedidos, Por_dia
# Register your models here.

admin.site.register(Pessoas)
admin.site.register(Custos)
admin.site.register(Pedidos)
admin.site.register(Por_dia)
