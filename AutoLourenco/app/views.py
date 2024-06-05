from django.shortcuts import render,redirect,get_object_or_404
from .models import Cliente,Agenda,Servicos,Carro
from .form import ClienteForm, AgendaForm,ServicosForm,CarroForm
from django.contrib import messages
from time import sleep
def home(request):
    return render(request,'home.html')

def clientes(request):
    filtro = request.GET.get('telemovel','')
    info = {}
    messages.success(request,'Ola')
    if filtro:
        info['clientes'] = Cliente.objects.filter(telemovel = filtro)
        return render(request,'lista_clientes.html',info)
    else:
        info['clientes'] = Cliente.objects.filter(perm='cliente')
        return render(request,'lista_clientes.html',info)

def novo_cliente(request):
    info = {}
    cliente_form = ClienteForm(request.POST or None)

    if cliente_form.is_valid():
        cliente_form.save()
    info['cliente_form'] = cliente_form
    return render(request,'cliente.html',info)

def carros(request):
    filtro = request.GET.get('matricula','')
    info = {}
    if filtro:
        info['carros'] = Carro.objects.filter(matricula = filtro)
        return render(request,'lista_carros.html',info)
    else:
        info['carros'] = Carro.objects.all()
        return render(request,'lista_carros.html',info)

def novo_carro(request):
    info = {}
    carro_form = CarroForm(request.POST or None)

    if carro_form.is_valid():
        carro_form.save()
        return redirect('url_carros')
    info['carro_form'] = carro_form
    return render(request,'carros.html',info)

def agendas(request):
    info = {}
    info['agendas'] = Agenda.objects.all()
    return render(request,'lista_agenda.html',info)
 
def nova_agenda(request):
    info = {}
    agenda_form = AgendaForm(request.POST or None)

    if agenda_form.is_valid():
        agenda_form.save()
        return redirect('url_agenda')

    info['agenda_form'] = agenda_form
    return render(request,'agenda.html',info)

def novo_servico(request):
    info = {}
    servico_form = ServicosForm(request.POST or None)

    if servico_form.is_valid():
        servico_form.save()
        return redirect('url_servicos')

    info['servico_form'] = servico_form
    return render(request,'servicos.html',info)

def servicos(request):  
    filtro = request.GET.get('matricula','')
    info = {}
    if filtro:
        info['filtro'] = Servicos.objects.filter(matricula = filtro)
        return render(request,'lista_servicos.html',info)
    else:
        info['filtro'] = Servicos.objects.all()
        return render(request,'lista_servicos.html',info)

def deleteagenda(request,id):
    form = get_object_or_404(Agenda,pk=id)
    form.delete()
    return redirect('/agenda')

def editagenda(request,id):
    edit = get_object_or_404(Agenda,pk=id)

    if(request.method =='POST'):
        edit.data = request.POST.get('data')
        edit.hora = request.POST.get('hora')
        edit.save()
        return redirect('/agenda')
    else:
        return render(request,'editagenda.html', {'edit':edit})

def deletecliente(request,telemovel):
    form = get_object_or_404(Cliente,pk=telemovel)
    form.delete()
    return redirect('/clientes')

def editcliente(request,telemovel):
    edit = get_object_or_404(Cliente,pk=telemovel)

    if(request.method =='POST'):
        edit.nome = request.POST.get('nome')
        edit.apelido = request.POST.get('apelido')
        edit.telemovel = request.POST.get('telemovel')
        edit.email = request.POST.get('email')
        edit.save()
        return redirect('/clientes')
    else:
        return render(request,'editcliente.html', {'edit':edit})


def deletecarro(request,matricula):
    form = get_object_or_404(Carro,pk=matricula)
    form.delete()
    return redirect('/carros')

def editcarros(request,matricula):
    edit = get_object_or_404(Carro,pk=matricula)

    if(request.method =='POST'):
        edit.marca = request.POST.get('marca')
        edit.modelo = request.POST.get('modelo')
        edit.matricula = request.POST.get('matricula')
        edit.ano = request.POST.get('ano')
        edit.save()
        return redirect('/carros')
    else:
        return render(request,'editcarros.html', {'edit':edit})

def deleteservico(request,id):
    form = get_object_or_404(Servicos,pk=id)
    form.delete()
    return redirect('/servicos')

def editservicos(request,id):
    edit = get_object_or_404(Servicos,pk=id)

    if(request.method =='POST'):
        edit.custo = request.POST.get('custo')
        edit.save()
        return redirect('/servicos')
    else:
        return render(request,'editservicos.html', {'edit':edit})
