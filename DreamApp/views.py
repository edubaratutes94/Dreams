from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from DreamApp import models, forms
from Dream import settings
import sweetify
from django.template.loader import render_to_string
from datetime import datetime
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _


# Create your views here.
def home(request):
    if request.POST:
        form = forms.SolicitudForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            text = form.cleaned_data['text']
            servicio = form.cleaned_data['servicio']
            solicitud = models.Solicitud(full_name=full_name, email=email, phone=phone, text=text, servicio=servicio)
            solicitud.save()

            entidad = models.General.objects.get()
            subject = _('Nueva Solicitud')
            message = render_to_string('dream_app/correo.html', {
                'reserva': solicitud,
            })
            send_mail(subject,
                      message,
                      settings.EMAIL_HOST_USER,
                      [entidad.email]  # destinatario
                      )
            sweetify.success(request, 'Solicitud realizada con éxito', button='Ok', timer=5000)
            return HttpResponseRedirect('/')
    services = models.Service.objects.all()
    info = models.Info_extra.objects.all()
    sponsor = models.Sponsor.objects.all()
    blog = models.Blog.objects.order_by("-id").all()[:3]
    tipo = models.Tipo_galery.objects.filter(active=True).all()
    fotos = models.Galery.objects.filter(active=True).all()[:6]
    return render(request, 'dream_app/inicio.html',
                  {'services': services, 'info': info, 'blog': blog, 'sponsor': sponsor, 'fotos': fotos, 'tipo': tipo})


def services(request):
    if request.POST:
        form = forms.SolicitudForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            text = form.cleaned_data['text']
            servicio = form.cleaned_data['servicio']
            solicitud = models.Solicitud(full_name=full_name, email=email, phone=phone, text=text, servicio=servicio)
            solicitud.save()

            entidad = models.General.objects.get()
            subject = _('Nueva Solicitud')
            message = render_to_string('dream_app/correo.html', {
                'reserva': solicitud,
            })
            send_mail(subject,
                      message,
                      settings.EMAIL_HOST_USER,
                      [entidad.email]  # destinatario
                      )
            sweetify.success(request, 'Solicitud realizada con éxito', button='Ok', timer=5000)
            return HttpResponseRedirect('/services/')
    services = models.Service.objects.all()
    planes = models.Planes.objects.all()
    return render(request, 'dream_app/services.html', {'services': services, 'planes': planes})


def blogs(request, index):
    blog = models.Blog.objects.order_by("-id").all()
    paginator = Paginator(blog, 3, index)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page_obj = paginator.page(paginator.num_pages)
    # page_obj = paginator.get_page(page_number)
    destacado = models.Blog.objects.filter(active=True).all()
    return render(request, 'dream_app/blog.html', {'page_obj': page_obj, 'destacado': destacado })


def blog_detail(request, pk):
    blog = get_object_or_404(models.Blog, pk=pk)
    try:
        the_next = blog.get_next_by_created_at()
    except:
        the_next = None
    try:
        the_prev = blog.get_previous_by_created_at()
    except:
        the_prev = None
    blogs = models.Blog.objects.exclude(pk=pk).order_by("-id").all()[:3]
    destacado = models.Blog.objects.filter(active=True).all()
    return render(request, 'dream_app/blog_details.html',
                  {'blog': blog, 'destacado': destacado, 'blogs': blogs, 'the_next': the_next, 'the_prev': the_prev})


# Funcion para la vista Contactos
def contact(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        comentario = models.Contact.objects.create(name=name, email=email, text=message)
        comentario.save()
        entidad = models.General.objects.get()
        subject = _('Nuevo Mensaje')
        message = render_to_string('dream_app/correo_contact.html', {
            'mensaje': comentario,
        })
        send_mail(subject,
                  message,
                  settings.EMAIL_HOST_USER,
                  [entidad.email]  # destinatario
                  )
        sweetify.success(request, 'Mensaje enviado con éxito', button='Ok', timer=5000)
        return HttpResponseRedirect("/contact/")
    return render(request, "dream_app/contact.html")

def team(request):
    team = models.Team.objects.all()
    return render(request, 'dream_app/team.html', {'team': team})


def about(request):
    info = models.Info_extra.objects.all()
    opiniones = models.Opinion.objects.all()
    team = models.Team.objects.all()
    return render(request, 'dream_app/about.html', {'info': info, 'opiniones': opiniones, 'team': team})


def galery(request):
    tipo = models.Tipo_galery.objects.all()
    fotos = models.Galery.objects.all()
    return render(request, 'dream_app/portfolio.html', {'fotos': fotos, 'tipo': tipo})
