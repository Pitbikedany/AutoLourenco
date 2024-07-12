from django.db import models

class Mecanico(models.Model):
    nome = models.CharField(max_length=100)
    telemovel = models.CharField(max_length=14, primary_key=True)
    perm = models.CharField(max_length=50, default='mecanico')

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=100)
    telemovel = models.CharField(max_length=14, primary_key=True)
    email = models.EmailField(max_length=100)
    perm = models.CharField(max_length=50, default='cliente')

    def __str__(self):
        return f"{self.nome} {self.apelido}"
    
class Carro(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20,primary_key=True)
    ano = models.IntegerField()
    telemovel = models.ForeignKey(Cliente,on_delete=models.CASCADE)

    def __str__(self)   :
        return self.matricula
    
class Agenda(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    matricula = models.ForeignKey(Carro,on_delete=models.CASCADE)
    telemovel = models.ForeignKey(Mecanico,on_delete=models.CASCADE)
    servico = models.TextField()

    def __str__(self):
        return self.servico

""" class Servicos(models.Model):
    matricula = models.ForeignKey(Carro, on_delete=models.CASCADE)
    servico = models.ForeignKey(Agenda,on_delete=models.CASCADE)
    custo = models.DecimalField(max_digits=7,decimal_places=2)

    def __str__(self):
        return self.matricula """

class Faturas(models.Model):
    matricula = models.ForeignKey(Carro,on_delete=models.CASCADE)
    data = models.DateField()

    def __str__(self):
        return self.data

class Item(models.Model):
    fatura = models.ForeignKey(Faturas, on_delete=models.CASCADE, related_name='itens')
    descricao = models.CharField(max_length=50)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=7,decimal_places=2)