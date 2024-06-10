from django.forms import ModelForm
from .models import Cliente,Agenda,Servicos,Carro,Mecanico,Faturas,Item

class MecanicoForm(ModelForm):
    class Meta:
        model = Mecanico
        fields = ['nome','telemovel']

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome','apelido','telemovel','email']

class CarroForm(ModelForm):
    class Meta:
        model = Carro
        fields = ['telemovel', 'marca','modelo','matricula','ano']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['telemovel'].empty_label = "Selecione um número "

class AgendaForm(ModelForm):
    class Meta:
        model = Agenda
        fields = ['data','hora','matricula','telemovel','servico']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['matricula'].empty_label = "Selecione uma matrícula "
        self.fields['telemovel'].empty_label = "Selecione um Mecânico "


class ServicosForm(ModelForm):
    class Meta:
        model = Servicos
        fields = ['matricula','servico','custo']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['matricula'].empty_label = "Selecione uma matrícula "
        self.fields['servico'].empty_label = "Selecione o serviço"

class FaturasForm(ModelForm):
    class Meta:
        model = Faturas
        fields = ['matricula','data']
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['matricula'].empty_label = "Selecione uma matrícula "

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['descricao','quantidade','preco','total']
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['matricula'].empty_label = "Selecione uma matrícula "