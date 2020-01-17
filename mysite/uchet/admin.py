from django.contrib import admin
from .models import Computer, CPU, RAM, HDD
# Register your models here.

class cpuInline(admin.TabularInline):
    model = CPU
    extra = 1

class ramInline(admin.TabularInline):
    model = RAM
    extra = 1

class hddInline(admin.TabularInline):
    model = HDD
    extra = 1

@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    inlines = [cpuInline, ramInline, hddInline]
    list_filter = ('inventory_number', 'manufacturer',
    'owner', 'status', 'last_service_date')

#admin.site.register(RAM)
#admin.site.register(HDD)
#admin.site.register(CPU)