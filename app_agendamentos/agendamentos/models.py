from django.db import models

class DadosGerais(models.Model):
    STATUS_CHOICES = [
        ('ANDAMENTO', 'Em andamento'),
        ('CONCLUÍDO', 'Concluído'),
    ]
    codigo_treinamento = models.IntegerField(null=False)
    treinamento =models.CharField(max_length=100, null=False)
    docente= models.CharField(max_length=100, null=False)
    proposta = models.CharField(max_length=120, null=False)
    empresa = models.CharField(max_length=120, null=False)
    cliente =models.CharField(max_length=100, null=False)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='ANDAMENTO')
    data_inicial =models.DateTimeField(null=False)
    data_final =models.DateTimeField(null=False)
    dias_treinamento = models.IntegerField(null=False)
    turno = models.CharField(max_length=15, null=False)
    horas = models.DateTimeField(null=False)
    observacao = models.TextField(blank=True)

    def __str__(self):
        return f"{self.treinamento} - {self.codigo_treinamento}"
    

