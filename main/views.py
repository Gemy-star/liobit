from django.shortcuts import render, redirect
from .models import ContactRequests, CategoryOfBusiness, Projects


def home_page(request):
    cats = CategoryOfBusiness.objects.all()
    return render(request, 'main/home.html', context={"cats": cats})


def about_page(request):
    return render(request, 'main/about.html')


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


def porjects(request, pk):
    projs = Projects.objects.filter(category=pk)
    context = {"projs": projs, "cat": CategoryOfBusiness.objects.get(pk=pk)}
    return render(request, 'main/projects.html', context=context)
