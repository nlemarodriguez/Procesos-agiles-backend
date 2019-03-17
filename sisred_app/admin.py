from django.contrib import admin
from .models import RED, ProyectoConectate, ProyectoRED, Version, Comentario, \
    Estado, HistorialEstados, Metadata, Notificacion, Recurso, Rol, RolAsignado, \
    Perfil, SubproductoRED, Propiedad

# Register your models here.
admin.site.register(RED)
admin.site.register(ProyectoConectate)
admin.site.register(ProyectoRED)
admin.site.register(Version)
admin.site.register(Comentario)
admin.site.register(Estado)
admin.site.register(HistorialEstados)
admin.site.register(Metadata)
admin.site.register(Notificacion)
admin.site.register(Recurso)
admin.site.register(Rol)
admin.site.register(RolAsignado)
admin.site.register(Perfil)
admin.site.register(SubproductoRED)
admin.site.register(Propiedad)
