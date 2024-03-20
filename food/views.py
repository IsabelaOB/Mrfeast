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
           
            return redirect('nombre_de_la_url')

    return render(request, 'login.html')


def home_view(request):
    # Lógica de la vista principal
    if request.method == 'GET' and 'siguiente_btn' in request.GET:
        # Si se presionó el botón "Siguiente", redirige a la página deseada
        return redirect('nombre_de_la')
    return render(request, 'home.html')
  
def inicio_view(request):
    # Puedes incluir la lógica que desees para la página de inicio
    mensaje_bienvenida = "¡Bienvenido a nuestra aplicación!"

    # Puedes pasar variables adicionales al contexto según tus necesidades
    context = {
        'mensaje_bienvenida': mensaje_bienvenida,
    }

    return render(request, 'inicio.html', context)