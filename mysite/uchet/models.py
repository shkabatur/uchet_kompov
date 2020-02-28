from django.db import models

# Create your models here.
class Printer(models.Model):
    inventory_number = models.CharField(max_length=20, default="",verbose_name="Инвентарный номер", unique=True)
    serial_number = models.CharField(max_length=20, default="",verbose_name="Серийный номер", unique=True)
    manufacturer = models.CharField(max_length=20, default="",verbose_name="Производитель") 
    owner = models.CharField(max_length=40, default="",verbose_name="Материально ответственный")
    last_service_date = models.DateTimeField(verbose_name="Дата последней проверки")
    comment = models.TextField(verbose_name="Комментарий", default="",blank=True)
    status = models.BooleanField(default=True, verbose_name="Исправность") 

    def __str__(self):
        return "Инв. № %s %s %s" % (self.inventory_number, self.manufacturer, self.owner)

    class Meta:
        verbose_name = "Принтер"
        verbose_name_plural = "Принтеры"
        

class Computer(models.Model):
    inventory_number = models.CharField(max_length=20, default="",verbose_name="Инвентарный номер", unique=True)
    manufacturer = models.CharField(max_length=20, default="",verbose_name="Производитель") 
    owner = models.CharField(max_length=40, default="",verbose_name="Материально ответственный")
    computer_name = models.CharField(max_length=20, default="",verbose_name="Имя компьютера", blank=True)
    last_service_date = models.DateTimeField(verbose_name="Дата последней проверки")
    comment = models.TextField(verbose_name="Комментарий", default="",blank=True)
    status = models.BooleanField(default=True, verbose_name="Исправность") 

    def __str__(self):
        return "Инв. № %s %s %s" % (self.inventory_number, self.manufacturer, self.owner)

    class Meta:
        verbose_name = "Компьютер"
        verbose_name_plural = "Компьютеры"
        

class RAM(models.Model):
    sn =  models.CharField(max_length=20, default="", verbose_name="Серийный номер", unique=True)
    manufacturer = models.CharField(max_length=20, default="", verbose_name="Производитель") 
    physical_size = models.CharField(max_length=8, verbose_name="Фромфактор") 
    amount = models.IntegerField(default=0, verbose_name="Размер (Гб)")        
    ram_type = models.CharField(max_length=6, verbose_name="Тип",)      
    speed = models.IntegerField(default=0, verbose_name="Скорость (Ггц)",)  
    status = models.BooleanField(default=True, verbose_name="Иправность")
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, verbose_name="Компьютер")

    def __str__(self):
        return "%s %s %dgb %dGHz" % (self.manufacturer, self.ram_type, self.amount, self.speed)

    class Meta:
        verbose_name = "Оперативная память"
        verbose_name_plural = "Оперативная память"

class CPU(models.Model):
    sn =  models.CharField(max_length=20, default="", verbose_name="Серийный номер", unique=True)
    manufacturer = models.CharField(max_length=20, default="", verbose_name="Производитель")
    socket = models.CharField(max_length=8, verbose_name="Сокет") 
    freequency = models.IntegerField(default=0, verbose_name="Частота")
    cores = models.IntegerField(default=0, verbose_name="Количество ядер")
    status = models.BooleanField(default=True, verbose_name="Иправность") 
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, verbose_name="Компьютер")

    def __str__(self):
        return "%s %s %dGHz cores: %d " % (self.manufacturer, self.socket, self.freequency, self.cores)

    class Meta:
        verbose_name = "Процессор"
        verbose_name_plural = "Процессоры"

class HDD(models.Model):
    sn =  models.CharField(max_length=20, default="", verbose_name="Серийный номер", unique=True)
    manufacturer = models.CharField(max_length=20, default="",verbose_name="Производитель") 
    hdd_type = models.CharField(max_length=6, verbose_name="Фромфактор") 
    capacity = models.IntegerField(default=0, verbose_name="Объём (Гб)")
    speed = models.IntegerField(default=0, verbose_name="Скорость")
    sdd = models.BooleanField(default=False, verbose_name="SSD?")
    status = models.BooleanField(default=True, verbose_name="Иправность")
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, verbose_name="Компьютер")

    def __str__(self):
        return "%s %s %dgb %d" % (self.manufacturer, self.hdd_type, self.capacity, self.speed)

    class Meta:
        verbose_name = "Жесткий диск"
        verbose_name_plural = "Жесткие диски"
    


    
