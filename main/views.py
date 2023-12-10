from django.shortcuts import render, redirect
from .models import ContactRequests, CategoryOfBusiness, Projects


def home_page(request):
    cats = CategoryOfBusiness.objects.all()
    return render(request, "main/home.html", context={"cats": cats})


def about_page(request):
    return render(request, "main/about.html")

def services_page(request):
    return render(request, "main/services.html")



def contact_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact = ContactRequests(personName=name, message=message, email=email)
        contact.save()
        if contact.pk:
            return redirect("home-page")
        else:
            return redirect("contact-page")
    return render(request, "main/contact_ar.html")


def porjects(request):
    return render(request, "main/projects.html")
