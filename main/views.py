from django.shortcuts import render, redirect
from .models import ContactRequests


def home_page(request):
    return render(request, 'main/home.html')


def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = ContactRequests(personName=name, message=message, email=email)
        contact.save()
        if contact.pk:
            return redirect('home-page')
        else:
            return redirect('contact-page')
    return render(request, 'main/contact.html')
