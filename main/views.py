from django.shortcuts import render, redirect
import smtplib
import email.message
from django.template.loader import render_to_string

def index(request):
    return render(request,'main/index.html')

def enviar_email(mail):
    corpo_email = render_to_string('main/email.html')

    msg = email.message.Message()
    msg['Subject'] = 'Validação do email ParkIn'
    msg['From'] = 'parkin2123@gmail.com'
    msg['To'] = mail
    password = 'vqybrhoxtqlbltnw'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('email enviado')

def contato(request):
    return render (request, "main/nos.html")

def a(request):
    return render(request, 'main/email.html')




