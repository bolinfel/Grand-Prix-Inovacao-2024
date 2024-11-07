from django.contrib import admin
from sensores.models import Sensor, Leituras, Local

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Sensor, AuthorAdmin)
admin.site.register(Leituras, AuthorAdmin)
admin.site.register(Local, AuthorAdmin)