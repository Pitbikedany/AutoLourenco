import datetime,sqlite3,smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#conexao com a base de dados
connection = sqlite3.connect('db.sqlite3')
conn = connection.cursor()
#query para selecionar a data
conn.execute('SELECT data FROM app_agenda')
query = conn.fetchall()

#adicionar datas a um array e fazer um while
savedata = []
for values in query:
    savedata.append(values[0])
i=0
while i<len(savedata):
    data = savedata[i]
    #dia
    dia1 = int(data[8])
    dia2 = int(data[9])
    diatotal = int(data[8:10])
    #mes
    mes1 = int(data[5])
    mes2 = int(data[6])
    mestotal = int(data[5:7])
    #ano
    ano = int(data[0:4])

    if dia1 == 0:
        dia = dia2
    else:
        dia = diatotal

    if mes1 == 0:
        mes = mes2
    else:
        mes = mestotal

    datapadrao = datetime.date(ano, mes, dia)
    hoje = datetime.date.today()

    if datapadrao > hoje:
        delta = datapadrao - hoje
    elif datapadrao <= hoje:
        delta = datapadrao - hoje

    check_data = False
    if delta.days <= 3 and delta.days >= 0:
        check_data = True
    else:
        check_data = False

    if check_data:
       pass

        # Configurações do servidor SMTP
        # smtp_server = 'smtp.gmail.com'
        # smtp_port = 587
        # smtp_user = 'danyslourenco@gmail.com'
        # smtp_password = 'Pasteleiro@12'
        # to_address = 'danyslourenco@gmail.com'
        # subject = 'MARCAÇÃO AUTO LOURENÇO'
        # body = 'teste'

        # # Criação da mensagem
        # msg = MIMEMultipart()
        # msg['From'] = smtp_user
        # msg['To'] = to_address
        # msg['Subject'] = subject

        # # Corpo do e-mail
        # msg.attach(MIMEText(body, 'plain'))

        # try:
        #     # Conectando ao servidor SMTP e enviando o e-mail
        #     server = smtplib.SMTP(smtp_server, smtp_port)
        #     server.starttls()
        #     server.login(smtp_user, smtp_password)
        #     server.send_message(msg)
        #     server.quit()

        #     print(f'E-mail enviado com sucesso para {to_address}')
        # except Exception as e:
        #     print(f'Erro ao enviar e-mail: {str(e)}')
    i+=1