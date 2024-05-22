from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from food.models import UserProfile
from django.http import HttpResponse
from .models import Menu
from pathlib import Path
import hashlib
import google.generativeai as genai
import markdown2
    
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
           
            return redirect('form')

    return render(request, 'login.html')


def home_view(request):
    # Lógica de la vista principal
    if request.method == 'GET' and 'siguiente_btn' in request.GET:
        # Si se presionó el botón "Siguiente", redirige a la página deseada
        menus = Menu.objects.all()
        return portal_view(request)
    return render(request, 'home.html')

def portal_view(request):
    busqueda = request.GET.get('busqueda')
    if busqueda:
        menus = Menu.objects.filter(title__icontains=busqueda)
    else:
        menus = Menu.objects.all()
    #movies = Movie.objects.all()
    return render(request, 'portal.html', {'menus':menus,})
    
   

  
def inicio_view(request):
    # Puedes incluir la lógica que desees para la página de inicio
    mensaje_bienvenida = "¡Bienvenido a nuestra aplicación!"

    # Puedes pasar variables adicionales al contexto según tus necesidades
    context = {
        'mensaje_bienvenida': mensaje_bienvenida,
    }

    return render(request, 'inicio.html', context)

def contacto_view(request):
    return render(request, 'contacto.html')

def generar_view(request):
    genai.configure(api_key="AIzaSyB5DIgYTBVipSNGwLfAK-RR470u3cEFIlI")
    generation_config = {
    "temperature": 0.9,
    "top_p": 0.95,
    "top_k": 32,
    "max_output_tokens": 10240,
    }
    safety_settings = [
    {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
     {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
     },
    {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
     "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
     },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest", generation_config=generation_config, safety_settings=safety_settings)
    mensaje = ""
    generateMenu = "Vas a actuar como un experto en recetas de todo tipo. Generame un menú con sus ingredientes, información nutricional y pasos de preparación a partir del siguiente mensaje: "
    if request.GET.get('generateMenu'):
        mensaje = request.GET.get('generateMenu')
        generateMenu = generateMenu + mensaje
    response = ""
    if generateMenu:
        response = model.generate_content(generateMenu).text
        response = markdown2.markdown(response)
    return render(request, 'generar.html', {'generateMenu':generateMenu, 'respuesta':response, 'mensaje':mensaje})