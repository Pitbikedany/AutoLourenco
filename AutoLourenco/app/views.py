from django.shortcuts import render,redirect,get_object_or_404
from .models import Cliente,Agenda,Carro,Faturas,Item
from .form import ClienteForm, AgendaForm,CarroForm,FaturasForm,ItemForm
from django.forms import inlineformset_factory
from .models import Cliente,Agenda,Carro
#from .models import Servicos
#from .form import ServicosForm
from .form import ClienteForm, AgendaForm,CarroForm
import sqlite3
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from django.http import FileResponse,HttpResponse
from django.contrib.staticfiles import finders
#funcao pagina principal
def home(request):
    return render(request,'home.html')

#funcao lista de clientes
def clientes(request):
    #request do telemovel para filtrar a pesquisa
    filtro = request.GET.get('telemovel','')
    info = {}
    if filtro:
        info['clientes'] = Cliente.objects.filter(telemovel = filtro)
        return render(request,'lista_clientes.html',info)
    else:
        info['clientes'] = Cliente.objects.filter(perm='cliente')
        return render(request,'lista_clientes.html',info)

#funcao para adicionar clientes
def novo_cliente(request):
    info = {}
    cliente_form = ClienteForm(request.POST or None)

    if cliente_form.is_valid():
        cliente_form.save()
        return redirect('url_clientes')
    info['cliente_form'] = cliente_form
    return render(request,'cliente.html',info)

#funcao lista de carros
def carros(request):
    #request da matricula para filtrar a pesquisa
    filtro = request.GET.get('matricula','')
    info = {}
    if filtro:
        info['carros'] = Carro.objects.filter(matricula = filtro)
        return render(request,'lista_carros.html',info)
    else:
        info['carros'] = Carro.objects.all()
        return render(request,'lista_carros.html',info)

#funcao para adicionar carros
def novo_carro(request):
    info = {}
    carro_form = CarroForm(request.POST or None)

    if carro_form.is_valid():
        carro_form.save()
        return redirect('url_carros')
    info['carro_form'] = carro_form
    return render(request,'carros.html',info)

#funcao para lista de agendas
def agendas(request):
    info = {}
    info['agendas'] = Agenda.objects.all()
    return render(request,'lista_agenda.html',info)
 
#funcao para adicionar agenda
def nova_agenda(request):
    info = {}
    agenda_form = AgendaForm(request.POST or None)

    if agenda_form.is_valid():
        agenda_form.save()
        return redirect('url_agenda')

    info['agenda_form'] = agenda_form
    return render(request,'agenda.html',info)

#funcao para adicionar servicos
# def novo_servico(request):
#     info = {}
#     servico_form = ServicosForm(request.POST or None)

#     if servico_form.is_valid():
#         servico_form.save()
#         return redirect('url_servicos')

#     info['servico_form'] = servico_form
#     return render(request,'servicos.html',info)

#funcao de lista de servicos
# def servicos(request): 
#     #request da matricula para filtrar a pesquisa 
#     filtro = request.GET.get('matricula','')
#     info = {}
#     if filtro:
#         info['filtro'] = Servicos.objects.filter(matricula = filtro)
#         return render(request,'lista_servicos.html',info)
#     else:
#         info['filtro'] = Servicos.objects.all()
#         return render(request,'lista_servicos.html',info)

#delete da agenda
def deleteagenda(request,id):
    #request da primary key para eliminar
    form = get_object_or_404(Agenda,pk=id)
    form.delete()
    return redirect('/agenda')

#edit da agenda
def editagenda(request,id):
    #request da primary key para editar
    edit = get_object_or_404(Agenda,pk=id)

    if(request.method =='POST'):
        #parametros do form agenda
        edit.data = request.POST.get('data')
        edit.hora = request.POST.get('hora')
        edit.save()
        return redirect('/agenda')
    else:
        return render(request,'editagenda.html', {'edit':edit})

#delete cliente
def deletecliente(request,telemovel):
    #request da primary key para eliminar
    form = get_object_or_404(Cliente,pk=telemovel)
    form.delete()
    return redirect('/clientes')

#edit do cliente
def editcliente(request,telemovel):
    #request da primary key para editar
    edit = get_object_or_404(Cliente,pk=telemovel)

    if(request.method =='POST'):
        #parametros do form cliente
        edit.nome = request.POST.get('nome')
        edit.apelido = request.POST.get('apelido')
        edit.telemovel = request.POST.get('telemovel')
        edit.email = request.POST.get('email')
        edit.save()
        return redirect('/clientes')
    else:
        return render(request,'editcliente.html', {'edit':edit})

#delete carro
def deletecarro(request,matricula):
    #request da primary key para eliminar
    form = get_object_or_404(Carro,pk=matricula)
    form.delete()
    return redirect('/carros')

#edit carro
def editcarros(request,matricula):
    #request da primary key para editar
    edit = get_object_or_404(Carro,pk=matricula)
    if(request.method =='POST'):
        #parametros do form carros
        edit.marca = request.POST.get('marca')
        edit.modelo = request.POST.get('modelo')
        edit.matricula = request.POST.get('matricula')
        edit.ano = request.POST.get('ano')
        edit.save()
        return redirect('/carros')
    else:
        return render(request,'editcarros.html', {'edit':edit})
    
""" #delete servicos
def deleteservico(request,id):
    #request da primary key para eliminar
    form = get_object_or_404(Servicos,pk=id)
    form.delete()
    return redirect('/servicos')

#edit servicos
def editservicos(request,id):
    #request da primary key para editar
    edit = get_object_or_404(Servicos,pk=id)

    if(request.method =='POST'):
        #parametros para form servicos
        edit.custo = request.POST.get('custo')
        edit.save()
        return redirect('/servicos')
    else:
        return render(request,'editservicos.html', {'edit':edit}) """

def nova_fatura(request):
    item_fatura = inlineformset_factory(Faturas, Item, form=ItemForm, extra=1)
    if request.method == 'POST':
        fatura_form = FaturasForm(request.POST)
        formset = item_fatura(request.POST)

        if fatura_form.is_valid() and formset.is_valid():
            fatura = fatura_form.save()
            itens = formset.save(commit=False)
            for item in itens:
                item.fatura = fatura
                item.save()
            return redirect('/faturas')
    else:
        fatura_form = FaturasForm()
        formset = item_fatura()
    return render(request, 'fatura.html', {'fatura_form': fatura_form, 'formset': formset})

def faturas(request):
    #request da matricula para filtrar a pesquisa 
    filtro = request.GET.get('matricula','')
    info = {}
    if filtro:
        info['filtro'] = Faturas.objects.filter(matricula = filtro)
        return render(request,'lista_faturas.html',info)
    else:
        info['filtro'] = Faturas.objects.all()
        return render(request,'lista_faturas.html',info)

def deletefatura(request,id):
    #request da primary key para eliminar
    form = get_object_or_404(Faturas,pk=id)
    form.delete()
    return redirect('/faturas')

def editfatura(request,id):
    #request da primary key para editar
    edit_fatura = get_object_or_404(Faturas, pk= id)

    if request.method =='POST':
        fatura_form = FaturasForm(request.POST, instance=edit_fatura)
        item_form = ItemForm(request.POST, instance=edit_fatura)

        if fatura_form.is_valid() and item_form.is_valid():
            edit_fatura = fatura_form.save()
            item_form.save()

    else:
        fatura_form = FaturasForm(request, instance=edit_fatura)
        item_form = ItemForm(request, instance=edit_fatura)
    return render(request,'editfatura.html', {'fatura_form':fatura_form},{'item_form':item_form})

def create_pdf(request,id):
    # Conectar a database
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()

    query_fatura = f"SELECT * FROM app_faturas WHERE id = {id}"
    cursor.execute(query_fatura)
    info_fatura = cursor.fetchall()
    fatura = []
    for values in info_fatura:
        fatura.append(values[1])
        fatura.append(values[2])

    query_carro = f"SELECT * FROM app_carro WHERE matricula = '{fatura[1]}'"
    cursor.execute(query_carro)
    info_carro = cursor.fetchall()
    carro = ""
    for values in info_carro:
        carro = values[0] + " " + values[1]
        telemovel = values[4]

    query_cliente = f"SELECT * FROM app_cliente WHERE telemovel = '{telemovel}'"
    cursor.execute(query_cliente)
    info_cliente = cursor.fetchall()
    cliente = ""

    for values in info_cliente:
        cliente = values[0] + " " + values[3]

    query_item = f"SELECT descricao FROM app_item WHERE fatura_id = {id}"
    cursor.execute(query_item)
    info_descricao = cursor.fetchall()

    descricao = []
    for values in info_descricao:
        descricao.append(values[0])

    query_item = f"SELECT quantidade FROM app_item WHERE fatura_id = {id}"
    cursor.execute(query_item)
    info_quantidade = cursor.fetchall()

    quantidade = []
    for values in info_quantidade:
        quantidade.append(values[0])

    query_item = f"SELECT preco FROM app_item WHERE fatura_id = {id}"
    cursor.execute(query_item)
    info_preco = cursor.fetchall()

    preco = []
    for values in info_preco:
        preco.append(values[0])


    total_item = []
    total_fatura = 0
    i = 0
    for value in quantidade:
        preco_total = quantidade[i] * preco[i]
        total_fatura += preco_total
        total_item.append(preco_total)
        i += 1

    company = 'Auto Lourenço'
    email = 'email@gmail.com'
    phone = '123456789'
    companyAddress = 'Avenida Oficina Mecanica Nº34'
    total = total_fatura
    client = cliente
    carbrand = carro
    invoiceNumber = fatura[1]

    file = fatura[0]+"_"+invoiceNumber+"_"+client+".pdf"
    #diretory = f"faturas\{file}"
    logo = finders.find('logo.png')
    my_canvas = canvas.Canvas(file, pagesize=A4)
    mystyle = ParagraphStyle('my style',fontName='Helvetica',fontSize=10,leading=15)
    my_canvas.setLineWidth(.5)
    my_canvas.setFont('Helvetica-Bold', 18)
    my_canvas.drawString(24, 817, company)
    my_canvas.setFont('Helvetica', 12)
    my_canvas.drawString(24, 800, companyAddress)
    my_canvas.drawString(24, 783, phone)
    my_canvas.drawString(24, 766, email)
    my_canvas.drawImage(logo, 460, 750, width=100, height=80)
    my_canvas.setFont('Helvetica-Bold', 15)
    my_canvas.drawCentredString(297.5, 735, 'Auto Service')
    my_canvas.setFont('Helvetica', 10)
    my_canvas.line(24, 740, 230, 740)
    my_canvas.line(360, 740, 571, 740)
    my_canvas.drawString(24, 720, 'Cliente :')
    my_canvas.drawString(75, 720, client)
    my_canvas.drawString(473, 720, 'Matrícula :')
    my_canvas.drawRightString(571, 720, invoiceNumber)
    my_canvas.drawString(24, 703, 'Carro :')
    my_canvas.drawString(75, 703, carbrand)
    my_canvas.drawString(474, 703, 'Data :')
    my_canvas.drawRightString(571, 703, fatura[0])

    my_canvas.line(24, 670, 571, 670)

    my_canvas.setFont('Helvetica-Bold', 9)

    my_canvas.drawCentredString(100 , 657, 'Descrição')
    my_canvas.drawCentredString(210, 657, 'Quantidade')
    my_canvas.drawCentredString(320, 657, 'Preço')
    my_canvas.drawCentredString(430, 657, 'Total')



    my_canvas.line(24, 650, 571, 650)
    my_canvas.setFont('Helvetica', 9)

    line_y = 650
    i = 0
    while i < len(descricao):

        if line_y <= 30 and line_y >= 0:

            my_canvas.showPage()
            my_canvas.setFont('Helvetica', 9)
            line_y = 817

            my_canvas.line(24, line_y, 571, line_y)

            line_y = line_y - 13

            my_canvas.drawCentredString(49 , line_y, str(descricao[i]))
            my_canvas.drawCentredString(144, line_y, str(quantidade[i]))
            my_canvas.drawCentredString(250, line_y, str(preco[i]) + "€")
            my_canvas.drawCentredString(350, line_y, str(total_item[i])+"€")


            line_y = line_y - 7

            my_canvas.line(24, line_y, 571, line_y)

        else:
            line_y = line_y - 13

            my_canvas.drawCentredString(100 , line_y, str(descricao[i]))
            my_canvas.drawCentredString(210, line_y, str(quantidade[i]))
            my_canvas.drawCentredString(320, line_y, str(preco[i])+"€")
            my_canvas.drawCentredString(430, line_y, str(total_item[i])+"€")

            line_y = line_y - 7

            my_canvas.line(24, line_y, 571, line_y)
        i+= 1
    if line_y >= 30 and line_y <= 70:
        line_y = line_y = 817
        my_canvas.showPage()
        my_canvas.setFont('Helvetica', 9)

    my_canvas.setFont('Helvetica-Bold', 10)
    my_canvas.drawRightString(500, line_y-20, 'Total :')

    total_euros = str(total) + "€"
    my_canvas.setFont('Helvetica', 10)
    my_canvas.drawRightString(571, line_y-20, str(total_euros))
    my_canvas.save()

    return FileResponse(as_attachment=True)