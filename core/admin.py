from django.contrib import admin
from .models import usuarios, solicitudesContacto,solicitudObra,obrasPublicadas

# Register your models here.
admin.site.register(usuarios)
admin.site.register(solicitudObra)
admin.site.register(solicitudesContacto)
admin.site.register(obrasPublicadas)