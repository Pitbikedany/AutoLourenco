from django.forms import ModelForm
from .models import Cliente,Agenda,Servicos,Carro,Mecanico


#formulario para criar mecanicos
class MecanicoForm(ModelForm):
    class Meta:
        model = Mecanico
        #parametros para mecanicos
        fields = ['nome','telemovel']

#formulario para criar clientes
class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        #parametros para clientes
        fields = ['nome','apelido','telemovel','email']

#formulario para criar carros
class CarroForm(ModelForm):
    class Meta:
        model = Carro
        #parametros para carro
        fields = ['telemovel', 'marca','modelo','matricula','ano']

    #funcao para o campo vazio do menu select
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['telemovel'].empty_label = "Selecione um número "

#formulario para criar agenda
class AgendaForm(ModelForm):
    class Meta:
        model = Agenda
        #parametros para agenda
        fields = ['data','hora','matricula','telemovel','servico']
    
    #funcao para o campo vazio do menu select
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['matricula'].empty_label = "Selecione uma matrícula "
        self.fields['telemovel'].empty_label = "Selecione um Mecânico "

#formulario para criar servicos
class ServicosForm(ModelForm):
    class Meta:
        model = Servicos
        #parametros para servicos
        fields = ['matricula','servico','custo']
    
    #funcao para o campo vazio do menu select
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['matricula'].empty_label = "Selecione uma matrícula "
        self.fields['servico'].empty_label = "Selecione o serviço"