from django.db import models

# Create your models here.

class RAM(models.Model):
    physical_size = models.CharField(max_length=20) #SODIMM
    amount = models.IntegerField(default=0)         #8gb
    ram_type = models.CharField(max_length=20)      #ddr4
    speed = models.IntegerField(default=0)          #2400

class CPU(models.Model):
    socket = models.CharField(max_length=20) 
    chipset = models.CharField(max_length=20)
    freequency = models.IntegerField(default=0)

class HDD(models.Model):
    hdd_type = models.CharField(max_length=20) 
    capacity = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)

class Computer(models.Model):
    ram = models.ForeignKey(RAM, on_delete=models.CASCADE)
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE)
    HDD = models.ForeignKey(HDD, on_delete=models.CASCADE)
    
