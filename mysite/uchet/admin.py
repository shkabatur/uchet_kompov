from django.contrib import admin
from .models import Computer, CPU, RAM, HDD
# Register your models here.

class cpuInline(admin.TabularInline):
    model = CPU

class ramInline(admin.TabularInline):
    model = RAM

class hddInline(admin.TabularInline):
    model = HDD

@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    inlines = [cpuInline, ramInline, hddInline]

#admin.site.register(RAM)
#admin.site.register(HDD)
#admin.site.register(CPU)