from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from food.models import UserProfile
from django.http import HttpResponse

    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Verifica si el usuario ya existe
        user = User.objects.filter(username=username).first()

        if user is None:
            # Si no existe, crea un nuevo usuario
            user = User.objects.create_user(username=username, password=password)
            UserProfile.objects.create(user=user)
        
        # Autentica al usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Puedes redirigir a la página que desees después del inicio de sesión exitoso
            return redirect('nombre_de_la_url')

    return render(request, 'login.html')


def home_view(request):
    # Lógica de la vista principal
    if request.method == 'GET' and 'siguiente_btn' in request.GET:
        # Si se presionó el botón "Siguiente", redirige a la página deseada
        return redirect('nombre_de_la')
    return render(request, 'home.html')  

