from django.shortcuts import render
from django.http import HttpResponse

def registro(request):
    return HttpResponse("Página de registro")

def login(request):
    return HttpResponse("Página de login")

def perfil(request):
    return HttpResponse("Página de perfil")
