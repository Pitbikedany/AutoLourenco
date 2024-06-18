from django.contrib import admin
from .models import Cliente,Agenda,Mecanico
# from .models import Servicos

admin.site.register(Cliente)
admin.site.register(Agenda)
# admin.site.register(Servicos)
admin.site.register(Mecanico)
