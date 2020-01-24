from django.contrib import admin
from .models import Computer, CPU, RAM, HDD
# Register your models here.

class cpuInline(admin.TabularInline):
    model = CPU
    extra = 0

class ramInline(admin.TabularInline):
    model = RAM
    extra = 0

class hddInline(admin.TabularInline):
    model = HDD
    extra = 0

@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    inlines = [cpuInline, ramInline, hddInline]
    list_display = ('inventory_number', 'manufacturer', 'owner', 'status', 'last_service_date')
    list_filter = ('manufacturer', 'owner', 'status', 'last_service_date', 'cpu', 'hdd', 'ram')
    search_fields = ('owner', 'manufacturer','inventory_number' )

#admin.site.register(RAM)
#admin.site.register(HDD)
#admin.site.register(CPU)