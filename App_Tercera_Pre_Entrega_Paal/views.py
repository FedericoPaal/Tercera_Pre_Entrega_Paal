from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import *
from .forms import *
from .carrito_compras import Carrito_Compras

# Create your views here.
def inicio(req):
    
    return render(req, "inicio.html")

def agregar_Novedad(req):       

    if req.method == "POST":
        novedad_formulario = Novedades_Formulario(req.POST, req.FILES)

        if novedad_formulario.is_valid():
            novedad_formulario.save()

            img = novedad_formulario.instance
            
            return render(req, "agregarNovedad.html", {"mi_formulario": novedad_formulario, "img": img})
    else:
        novedad_formulario = Novedades_Formulario()
    return render(req, "agregarNovedad.html", {"mi_formulario": novedad_formulario})
    
def eliminar_Novedad(req, id):
    if req.method == "POST":

        novedad = Novedad.objects.get(id=id)
        novedad.delete()

        novedades = Novedad.objects.all().order_by("id").reverse()
        
        return render(req, "novedad.html", {"novedades": novedades})
    

def editar_Novedad(req, id):

    novedad = Novedad.objects.get(id=id) 

    if req.method == "POST":
        mi_formulario = Novedades_Formulario(req.POST, req.FILES, instance=novedad)

        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data
            novedad.titulo = data["titulo"]
            novedad.autor = data["autor"]
            novedad.precio = data["precio"]
            novedad.imagen = data["imagen"]
            mi_formulario.save()
            
            return render(req, "inicio.html")
    else:
        mi_formulario = Novedades_Formulario(initial={
            "titulo": novedad.titulo,
            "autor": novedad.autor, 
            "precio": novedad.precio,
            "imagen": novedad.imagen,
        })
        return render(req, "editarNovedad.html", {"mi_formulario": mi_formulario, "id": novedad.id})


def agregar_Libro(req):

    if req.method == "POST":
        libro_formulario = Libros_Formulario(req.POST, req.FILES)

        if libro_formulario.is_valid():
            libro_formulario.save()

            img = libro_formulario.instance
            
            return render(req, "agregarLibro.html", {"mi_formulario": libro_formulario, "img": img})
    else:
        libro_formulario = Libros_Formulario()
    return render(req, "agregarLibro.html", {"mi_formulario": libro_formulario})
    
def eliminar_Libro(req, id):
    if req.method == "POST":

        libro = Libro.objects.get(id=id)
        libro.delete()

        libros = Libro.objects.all().order_by("id").reverse()
        
        return render(req, "libro.html", {"libros": libros})
    
def editar_Libro(req, id):

    libro = Libro.objects.get(id=id) 

    if req.method == "POST":
        mi_formulario = Libros_Formulario(req.POST, req.FILES, instance=libro)

        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data
            libro.titulo = data["titulo"]
            libro.autor = data["autor"]
            libro.precio = data["precio"]
            libro.imagen = data["imagen"]
            mi_formulario.save()
            
            return render(req, "inicio.html")
    else:
        mi_formulario = Libros_Formulario(initial={
            "titulo": libro.titulo,
            "autor": libro.autor, 
            "precio": libro.precio,
            "imagen": libro.imagen,
        })
        return render(req, "editarLibro.html", {"mi_formulario": mi_formulario, "id": libro.id})


def agregar_Merchandising(req):

    if req.method == "POST":
        merchandising_formulario = Merchandising_Formulario(req.POST, req.FILES)

        if merchandising_formulario.is_valid():
            merchandising_formulario.save()

            img = merchandising_formulario.instance
            
            return render(req, "agregarMerchandising.html", {"mi_formulario": merchandising_formulario, "img": img})
    else:
        merchandising_formulario = Merchandising_Formulario()
    return render(req, "agregarMerchandising.html", {"mi_formulario": merchandising_formulario})
   

def eliminar_Merchandising(req, id):
    if req.method == "POST":

        merchandising = Merchandising.objects.get(id=id)
        merchandising.delete()

        merchandisings = Merchandising.objects.all().order_by("id").reverse()
        
        return render(req, "merchandising.html", {"merchandisings": merchandisings})
    

def editar_Merchandising(req, id):

    merchandising = Merchandising.objects.get(id=id) 

    if req.method == "POST":
        mi_formulario = Merchandising_Formulario(req.POST, req.FILES, instance=merchandising)

        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data
            merchandising.titulo = data["titulo"]
            merchandising.precio = data["precio"]
            merchandising.imagen = data["imagen"]
            mi_formulario.save()
            
            return render(req, "inicio.html")
    else:
        mi_formulario = Merchandising_Formulario(initial={
            "titulo": merchandising.titulo, 
            "precio": merchandising.precio,
            "imagen": merchandising.imagen,
        })
        return render(req, "editarMerchandising.html", {"mi_formulario": mi_formulario, "id": merchandising.id})
    

@login_required
def consulta(req):

    if req.method == "POST":
        consulta_formulario = Consultas_Formulario(req.POST)

        if consulta_formulario.is_valid():
            data = consulta_formulario.cleaned_data
            _consulta = Consulta(nombre=data["nombre"], email=data["email"], consulta=data["consulta"])
            _consulta.save()
            
            return render(req, "inicio.html")
    else:
        consulta_formulario = Consultas_Formulario()
        return render(req, "consulta.html", {"mi_formulario": consulta_formulario})
    
def eliminar_Consulta(req, id):
    if req.method == "POST":
        consulta = Consulta.objects.get(id=id)
        consulta.delete()

        consultas = Consulta.objects.all()
        return render(req, "consulta.html", {"consultas": consultas})
    

def busqueda_objetos(req):
    return render(req, "inicio.html")

def buscar(req: HttpRequest):

    if req.GET["producto"]:
        producto = req.GET["producto"]
        
        productos = Libro.objects.filter(titulo__icontains=producto)  

        return render(req, "inicio.html", {"productos": productos})
    
    else:
        return render(req, "inicio.html")


def loginView(req):

    if req.method == "POST":
        
        mi_formulario = AuthenticationForm(req, data=req.POST)

        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data
            usuario = data["username"]
            contrasena = data["password"]

            user = authenticate(username=usuario, password=contrasena)
            
            if user:
                login(req, user)
                return render(req, "inicio.html", {"mensaje": f"Bienvenido/a {usuario}!"})
            
        return render(req, "inicio.html", {"mensaje2": f"Usuario y/o contraseña incorrectos. Pruebe de nuevo por favor."})

    else:
        mi_formulario = AuthenticationForm()
        return render(req, "login.html", {"mi_formulario": mi_formulario})
    

def register(req):

    if req.method == "POST":
        
        mi_formulario = UserCreationForm(req.POST)

        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data
            usuario = data["username"]
            mi_formulario.save()
            return render(req, "inicio.html", {"mensaje": f"Usuario {usuario} creado con éxito!"})

        return render(req, "inicio.html", {"mensaje2": f"Repita correctamente la contraseña"})

    else:
        mi_formulario = UserCreationForm()
        return render(req, "registro.html", {"mi_formulario": mi_formulario})
    

def editar_perfil(req):

    usuario = req.user

    if req.method == 'POST':

        mi_formulario = UserEditForm(req.POST, instance=req.user)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            usuario.save()

            return render(req, "editarUsuario.html", {"mi_formulario": mi_formulario, "mensaje": "El usuario ha sido actualizado con éxito"})
        else:
            return render(req, "editarUsuario.html", {"mi_formulario": mi_formulario})
    
    else:
        mi_formulario = UserEditForm(instance=usuario)
        return render(req, "editarUsuario.html", {"mi_formulario": mi_formulario})


def agregar_avatar(req):    #NO SE USA

    if req.method == 'POST':

        mi_formulario = Avatar_Formulario(req.POST, req.FILES)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data
            avatar = Avatar(user=req.user, imagen=data["imagen"])
            avatar.save()

            return render(req, "agregarAvatar.html", {"mensaje": "El avatar ha sido actualizado con éxito"})
    
    else:
        mi_formulario = Avatar_Formulario()
        return render(req, "agregarAvatar.html", {"mi_formulario": mi_formulario})


def crea_cliente(req):

    if req.method == "POST":
        
        info = req.POST

        mi_formulario = Cliente_Formulario({
            "nombre": info["nombre"],
            "apellido": info["apellido"],
            "email": info["email"]
        })

        userForm = UserCreationForm({
            "username": info["username"],
            "password1": info["password1"],
            "password2": info["password2"]
        })

        if mi_formulario.is_valid() and userForm.is_valid():
            
            data = mi_formulario.cleaned_data
            data.update(userForm.cleaned_data)

            user =User(username=data["username"])
            user.set_password(data["password1"])
            user.save()

            cliente = Cliente(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], user=user)
            cliente.save()

            return render(req, "inicio.html", {"mensaje": "Usuario creado con éxito"})

    else:

        mi_formulario = Cliente_Formulario()
        userForm = UserCreationForm()
        return render(req, "clienteFormulario.html", {"mi_formulario": mi_formulario, "userForm": userForm})
    

def about_me(req):
    return render(req, "aboutMe.html")


def carrito_compras(req):

    productos = req.session.get("carrito")

    return render(req, "carrito.html", {"productos": productos})

def lista_consultas(req):

    consultas = Consulta.objects.all()
    return render(req, "consulta.html", {"consultas": consultas})


def libros(req):

    libros = Libro.objects.all().order_by("id").reverse()
    return render(req, "libro.html", {"libros": libros})


def novedades(req):

    novedades = Novedad.objects.all().order_by("id").reverse()
    return render(req, "novedad.html", {"novedades": novedades})


def merchs(req):

    merchs = Merchandising.objects.all().order_by("id").reverse()
    return render(req, "merchandising.html", {"merchs": merchs})

#Productos

def comprar(req):

    carrito = Carrito_Compras(req)
    carrito.limpiar_carrito()
    productos = req.session.get("carrito")
    
    return render(req, "carrito.html", {"mensaje": "La compra de sus producto/s ha sido exitosa! Gracias por elegirnos!", "productos": productos})

def agregar_producto(req, producto_id):
    
    carrito = Carrito_Compras(req)
    libro = Libro.objects.get(id=producto_id)
    carrito.agregar(libro)
    productos = req.session.get("carrito")

    return render(req, "carrito.html", {"productos": productos})


def eliminar_producto(req, producto_id):
    
    carrito = Carrito_Compras(req)
    libro = Libro.objects.get(id=producto_id)
    carrito.eliminar(libro)
    productos = req.session.get("carrito")

    return render(req, "carrito.html", {"productos": productos})


def restar_producto(req, producto_id):
    
    carrito = Carrito_Compras(req)
    libro = Libro.objects.get(id=producto_id)
    carrito.restar_producto(libro)
    productos = req.session.get("carrito")

    return render(req, "carrito.html", {"productos": productos})


def limpiar_carrito(req):
    
    carrito = Carrito_Compras(req)
    carrito.limpiar_carrito()
    productos = req.session.get("carrito")
    return render(req, "carrito.html", {"productos": productos})



def ver_detalles_libro(req, producto_id):

    libro = Libro.objects.get(id=producto_id)
    return render(req, "detallesLibro.html", {"libro": libro})


def ver_detalles_novedad(req, producto_id):

    novedad = Novedad.objects.get(id=producto_id)
    return render(req, "detallesNovedad.html", {"novedad": novedad})


def ver_detalles_merch(req, producto_id):

    merch = Merchandising.objects.get(id=producto_id)
    return render(req, "detallesMerchandising.html", {"merch": merch})


def sin_pagina(req):
    return render(req, "sinPagina.html")