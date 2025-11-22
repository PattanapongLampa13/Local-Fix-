from django.shortcuts import render

# Create your views here.
def menu(request):
    return render(request, "menu.html")
def home(request):
    return render(request, "home.html")
def contact(request):
    return render(request, "contact.html")