from django.contrib import admin
from .models import Novedad, Libro, Merchandising, Consulta, Consultas_Clientes, Avatar

# Register your models here.
admin.site.register(Novedad)
admin.site.register(Libro)
admin.site.register(Merchandising)
admin.site.register(Consulta)
admin.site.register(Consultas_Clientes)
admin.site.register(Avatar)