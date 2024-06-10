from django.contrib import admin
from django.urls import path,reverse
from app.views import home,novo_cliente,clientes,agendas,nova_agenda,novo_servico,servicos,carros,novo_carro,deleteagenda,deletecliente,deletecarro
from app.views import deleteservico,editcliente,editcarros,editagenda,editservicos,gen_pdf,nova_fatura,faturas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='url_home'),
    path('novocliente/',novo_cliente, name='url_novo_cliente'),
    path('clientes/',clientes,name="url_clientes"),
    path('carros/',carros,name="url_carros"),
    path('novocarro/',novo_carro,name="url_novo_carro"),
    path('agenda/',agendas,name='url_agenda'),
    path('novaagenda/',nova_agenda,name='url_nova_agenda'),
    path('novoservico/',novo_servico,name='url_novo_servico'),
    path('servicos/',servicos,name='url_servicos'),
    path('agenda/deleteagenda/<int:id>',deleteagenda, name='delete-agenda'),
    path('agenda/editagenda/<int:id>',editagenda, name='edit-agenda'),
    path('clientes/deletecliente/<str:telemovel>',deletecliente, name='delete-cliente'),
    path('clientes/editcliente/<str:telemovel>',editcliente, name='edit-cliente'),
    path('carros/deletecarro/<str:matricula>',deletecarro, name='delete-carro'),
    path('carros/editcarro/<str:matricula>',editcarros, name='edit-carro'),
    path('servicos/deleteservico/<int:id>',deleteservico, name='delete-servico'),
    path('servicos/editservico/<int:id>',editservicos, name='edit-servico'),
    path('pdfs',gen_pdf, name='criar-pdf'),
    path('novafatura/',nova_fatura, name='url_nova_fatura'),
    path('listafaturas/',faturas, name='url_faturas'),





]
