from django.shortcuts import render
import random

def inicio(request):
    return render(request, 'juegos/inicio.html')

def menu_juegos(request):
    return render(request, 'juegos/menu_juegos.html')

def sopa_letras(request):
    palabras = ["PYTHON", "DJANGO", "HTML", "CSS", "JAVASCRIPT", "BOOTSTRAP"]
    return render(request, 'juegos/sopa_letras.html', {'palabras': palabras})

def palabras(request):
    return render(request, 'juegos/palabras.html')


def dictado(request):
    frases = [
        "El rápido zorro marrón salta sobre el perro perezoso",
        "Python es un lenguaje de programación poderoso",
        "Django hace el desarrollo web fácil y rápido",
        "La práctica hace al maestro",
        "Aprender es un viaje continuo",
        "El conocimiento es poder",
        "HTML CSS y JavaScript son tecnologías web",
        "Desarrollador web es una profesión en crecimiento",
        "Python se usa para inteligencia artificial",
        "Django sigue el patrón modelo vista controlador"
    ]
    frase_actual = random.choice(frases)
    return render(request, 'juegos/dictado.html', {
        'frase_actual': frase_actual,
        'frases_todas': frases  
        
    })