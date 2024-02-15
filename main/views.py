from django.shortcuts import render, redirect
import smtplib
import email.message
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@csrf_protect
def index(request):
    return render(request,'main/index.html')

@csrf_protect
def enviar_email(mail):
    corpo_email = render_to_string('main/email.html')

    msg = email.message.Message()
    msg['Subject'] = 'Validação do email ParkIn'
    msg['From'] = 'parkin2123@gmail.com'
    msg['To'] = mail
    password = 'acozatwlaflsvqdh'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('email enviado')

@csrf_protect
def a(request):
    return render(request, 'main/email.html')

@login_required
def fazer_logout(request):
    logout(request)
    return redirect('/')