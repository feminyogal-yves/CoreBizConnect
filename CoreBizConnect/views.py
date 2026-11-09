from django.shortcuts import render, redirect
from .models import ContactMessage


def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

    return redirect('/coreBizConnect/index/?success=1')

    return redirect('/coreBizConnect/index/')
