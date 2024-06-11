from django.contrib import admin
from django.urls import path,reverse
from app.views import home,novo_cliente,clientes,agendas,nova_agenda,novo_servico,servicos,carros,novo_carro,deleteagenda,deletecliente,deletecarro
from app.views import deleteservico,editcliente,editcarros,editagenda,editservicos,gen_pdf,nova_fatura,faturas

urlpatterns = [
    path('admin/', admin.site.urls),
    #home page
    path('', home, name='url_home'),
    #add cliente
    path('novocliente/',novo_cliente, name='url_novo_cliente'),
    #lista clientes
    path('clientes/',clientes,name="url_clientes"),
    #lista carros
    path('carros/',carros,name="url_carros"),
    #add carro
    path('novocarro/',novo_carro,name="url_novo_carro"),
    #lista agenda
    path('agenda/',agendas,name='url_agenda'),
    #add agenda
    path('novaagenda/',nova_agenda,name='url_nova_agenda'),
    #add servicos
    path('novoservico/',novo_servico,name='url_novo_servico'),
    #lista servicos
    path('servicos/',servicos,name='url_servicos'),
    #delete agenda
    path('agenda/deleteagenda/<int:id>',deleteagenda, name='delete-agenda'),
    #edit agenda
    path('agenda/editagenda/<int:id>',editagenda, name='edit-agenda'),
    #delete clientes
    path('clientes/deletecliente/<str:telemovel>',deletecliente, name='delete-cliente'),
    #edit clientes
    path('clientes/editcliente/<str:telemovel>',editcliente, name='edit-cliente'),
    #delete carros
    path('carros/deletecarro/<str:matricula>',deletecarro, name='delete-carro'),
    #edit carros
    path('carros/editcarro/<str:matricula>',editcarros, name='edit-carro'),
    #delete servicos
    path('servicos/deleteservico/<int:id>',deleteservico, name='delete-servico'),
    #edit servicos
    path('servicos/editservico/<int:id>',editservicos, name='edit-servico'),
    path('pdfs',gen_pdf, name='criar-pdf'),
    path('novafatura/',nova_fatura, name='url_nova_fatura'),
    path('listafaturas/',faturas, name='url_faturas'),





]
