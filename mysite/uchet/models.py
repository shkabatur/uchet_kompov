from django.db import models

# Create your models here.

class RAM(models.Model):
    manufacturer = models.CharField(max_length=20, default="", verbose_name="Производитель") 
    physical_size = models.CharField(max_length=20, verbose_name="Фромфактор") 
    amount = models.IntegerField(default=0, verbose_name="Размер")        
    ram_type = models.CharField(max_length=20, verbose_name="Тип",)      
    speed = models.IntegerField(default=0, verbose_name="Скорость",)  
    status = models.BooleanField(default=True, verbose_name="Иправность")    

    def __str__(self):
        return "%s %s %dgb %dGHz" % (self.manufacturer, self.ram_type, self.amount, self.speed)

    class Meta:
        verbose_name = "Оперативная память"
        verbose_name_plural = "Оперативная память"

class CPU(models.Model):
    manufacturer = models.CharField(max_length=20, default="", verbose_name="Производитель")
    socket = models.CharField(max_length=20, verbose_name="Сокет") 
    freequency = models.IntegerField(default=0, verbose_name="Частота")
    cores = models.IntegerField(default=0, verbose_name="Количество ядер")
    status = models.BooleanField(default=True, verbose_name="Иправность") 

    def __str__(self):
        return "%s %s %dGHz cores: %d " % (self.manufacturer, self.socket, self.freequency, self.cores)

    class Meta:
        verbose_name = "Процессор"
        verbose_name_plural = "Процессоры"

class HDD(models.Model):
    manufacturer = models.CharField(max_length=20, default="",verbose_name="Производитель") 
    hdd_type = models.CharField(max_length=20, verbose_name="Фромфактор") 
    capacity = models.IntegerField(default=0, verbose_name="Объём")
    speed = models.IntegerField(default=0, verbose_name="Скорость")
    status = models.BooleanField(default=True, verbose_name="Иправность")

    def __str__(self):
        return "%s %s %dgb %d" % (self.manufacturer, self.hdd_type, self.capacity, self.speed)

    class Meta:
        verbose_name = "Жесткий диск"
        verbose_name_plural = "Жесткие диски"
    

class Computer(models.Model):
    inventory_number = models.CharField(max_length=20, default="",verbose_name="Инвентарный номер")
    manufacturer = models.CharField(max_length=20, default="",verbose_name="Производитель") 
    owner = models.CharField(max_length=20, default="",verbose_name="Материально ответственный")
    ram = models.ForeignKey(RAM, on_delete=models.CASCADE, verbose_name="Оперативная память")
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE, verbose_name="Процессор")
    hdd = models.ForeignKey(HDD, on_delete=models.CASCADE, verbose_name="Жесткий диск",)
    last_service_date = models.DateTimeField(verbose_name="Дата последней проверки")
    status = models.BooleanField(default=True, verbose_name="Иправность") 

    def __str__(self):
        return "%s %s %s %s" % (self.manufacturer, self.owner, self.cpu, self.inventory_number)

    class Meta:
        verbose_name = "Компьютер"
        verbose_name_plural = "Компьютеры"
        
    
