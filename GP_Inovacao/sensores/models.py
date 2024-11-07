from django.db import models

class Local(models.Model):
    MaqLin = models.CharField(verbose_name="Maquina ou Linha", max_length=3)
    Setor = models.CharField(verbose_name="Setor", max_length=20)
    Linha = models.CharField(verbose_name="Linha", max_length=20)
    Obs = models.CharField(verbose_name="Observações", max_length=30)

class Sensor(models.Model):
    FK_Local = models.ForeignKey(Local, verbose_name="Local", on_delete=models.CASCADE)

class Leituras(models.Model):
    FK_Sensor = models.ForeignKey(Sensor, verbose_name="Sensor", on_delete=models.CASCADE)
    ValorA = models.FloatField(verbose_name="Valor Lido A")
    ValorB = models.FloatField(verbose_name="Valor Lido B")
    Data = models.DateTimeField(verbose_name="Data da Leitura")