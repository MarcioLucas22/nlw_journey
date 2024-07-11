import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_addrs, body):
    from_addr = 'inserir email'
    login = 'colocar login'
    password = 'colocar senha'

    msg = MIMEMultipart()
    msg['from'] = 'viagens_confirmar@email.com'
    msg['to'] = ', '.join(to_addrs)

    msg['Subject'] = 'Confirmação de Viagem!'
    msg.attach(MIMEText(body, 'plain'))