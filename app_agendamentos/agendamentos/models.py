from django.db import models

#Tabela docente
class Docente(models.Model):
    nome= models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nome
    
#tabela cliente    
class Cliente(models.Model):
    nome= models.CharField(max_length=50, null=False)
    regiao = models.CharField(max_length=15, null=True)

    def __str__(self):
        return f"{self.nome} - {self.regiao}"
    
 #tabela treinamento   
class Treinamento(models.Model):
    TREINAMENTO_CHOICES = [
        ('EAD', 'EAD'),
        ('PRESENCIAL', 'Presencial'),
    ]
    nome= models.CharField(max_length=50, null=False)
    formacao= models.TimeField(null=False)
    modalidade= models.CharField(max_length=15, choices= TREINAMENTO_CHOICES, null=False)

    def __str__(self):
        return self.nome
     
#Tabela Cadastro Agendamento Principal
class DadosGerais(models.Model):
    STATUS_CHOICES = [
        ('ANDAMENTO', 'Em andamento'),
        ('CONCLUÍDO', 'Concluído'),
    ]
    treinamento =models.ForeignKey(Treinamento, on_delete=models.CASCADE, related_name="dados_gerais")
    docente= models.ForeignKey(Docente, on_delete=models.CASCADE, related_name="dados_gerais")#related_name="dados_gerais": Isso permite acessar todos os treinamentos de um docente usando docente.dados_gerais.all()
    proposta = models.CharField(max_length=120, null=False)
    empresa = models.CharField(max_length=120, null=False)
    cliente =models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="dados_gerais")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='ANDAMENTO')
    data_inicial =models.DateTimeField(null=False)
    data_final =models.DateTimeField(null=False)
    dias_treinamento = models.IntegerField(null=False)
    turno = models.CharField(max_length=15, null=False)
    horas = models.TimeField(null=False)
    observacao = models.TextField(blank=True)

    def __str__(self):
        return f"{self.treinamento} - {self.cliente}"
    



 

    


    

