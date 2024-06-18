import sqlite3
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

# Conectar a database
connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

id = 16

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

company = "Auto Lourenço"
email = "jose.rosa.lourenco@gmail.com"
phone = "+351 966 306 406"
companyAddress = "Rua Adolfo Simões Muller Nº3"
total = total_fatura
discount = "Desconto"
payment = total_fatura
client = cliente
carbrand = carro
invoiceNumber = fatura[1]

file = invoiceNumber+"_"+client+".pdf"
my_canvas = canvas.Canvas(file, pagesize=A4)
mystyle = ParagraphStyle('my style',fontName='Helvetica',fontSize=10,leading=15)
my_canvas.setLineWidth(.5)
my_canvas.setFont('Helvetica-Bold', 18)
my_canvas.drawString(24, 817, company)
my_canvas.setFont('Helvetica', 12)
my_canvas.drawString(24, 800, companyAddress)
my_canvas.drawString(24, 783, phone)
my_canvas.drawString(24, 766, email)
# my_canvas.drawImage("logo.png", 460, 750, width=100, height=80)
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
        my_canvas.drawCentredString(250, line_y, str(preco[i]))
        my_canvas.drawCentredString(350, line_y, str(total_item[i]))


        line_y = line_y - 7

        my_canvas.line(24, line_y, 571, line_y)

    else:
        line_y = line_y - 13

        my_canvas.drawCentredString(100 , line_y, str(descricao[i]))
        my_canvas.drawCentredString(210, line_y, str(quantidade[i]))
        my_canvas.drawCentredString(320, line_y, str(preco[i]))
        my_canvas.drawCentredString(430, line_y, str(total_item[i]))

        line_y = line_y - 7

        my_canvas.line(24, line_y, 571, line_y)
    i+= 1
if line_y >= 30 and line_y <= 70:
    line_y = line_y = 817
    my_canvas.showPage()
    my_canvas.setFont('Helvetica', 9)

my_canvas.setFont('Helvetica-Bold', 10)
my_canvas.drawRightString(500, line_y-20, 'Total :')
my_canvas.drawRightString(500, line_y-35, 'Discount :')
my_canvas.drawRightString(500, line_y-50, 'Payment :')

my_canvas.setFont('Helvetica', 10)
my_canvas.drawRightString(571, line_y-20, str(total))
my_canvas.drawRightString(571, line_y-35, str(discount))
my_canvas.drawRightString(571, line_y-50, str(payment))
my_canvas.save()