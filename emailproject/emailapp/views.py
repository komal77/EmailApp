from django.shortcuts import render
from emailproject.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail, EmailMessage

def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = str(sub['sub'].value())
        message = str(sub['body'].value())
        recepient = str(sub['Email'].value())
        attachment = request.FILES['attachment']
        mail = EmailMessage(subject, 
            message, EMAIL_HOST_USER, [recepient]) #fail_silently = False)
        mail.attach(attachment.name, attachment.read(), attachment.content_type)
        mail.send()
        return render(request, 'success.html', {'recepient': recepient})
    return render(request, 'index.html', {'form':sub})