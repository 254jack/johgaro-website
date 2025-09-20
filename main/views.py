from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ContactMessage
from .forms import ContactForm
from django.core.mail import EmailMessage,BadHeaderError
from django.contrib import messages
import socket
import smtplib

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
def beans(request):
    return render(request, 'beans.html')
def corns(request):
    return render(request, 'maize.html')
def peas(request):
    return render(request, 'peas.html')

def wheat(request):
    return render(request, 'wheat.html')

def contact(request):
    return render(request, 'contact.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()

            subject = f"New Contact Message from {contact.name}"
            message = f"Name: {contact.name}\nEmail: {contact.email}\n\nMessage:\n{contact.message}"
            from_email = 'taixonj@gmail.com'
            recipient_list = ['taixonj@gmail.com']

            try:
                email = EmailMessage(
                    subject=subject,
                    body=message,
                    from_email=from_email,
                    to=recipient_list,
                    reply_to=[contact.email],
                )
                email.send()
                messages.success(request, 'Your message has been sent successfully.')
                return redirect('contact')

            except (socket.gaierror, socket.timeout, smtplib.SMTPException):
                return render(request, 'email_error.html')
            except BadHeaderError:
                return render(request, 'email_error.html')
            except Exception:
                return render(request, 'email_error.html')

    else:
        form = ContactForm()
        
    return render(request, 'contact.html', {'form': form})