from django.contrib import admin
from .models import Computer, CPU, RAM, HDD
# Register your models here.

admin.site.register(Computer)
admin.site.register(RAM)
admin.site.register(HDD)
admin.site.register(CPU)