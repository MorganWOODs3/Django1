from django.shortcuts import render

# Create your views here.
def bonjour(request):
    return render(request,'monapli/bonjour.html')

def saisie(request):
    return render(request,'monapli/saisie.html')

def traitement(request):
    nom = request.GET["nom"]
    return render(request, "monapli/traitement.html",{"nom":nom})