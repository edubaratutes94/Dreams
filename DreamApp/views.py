from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render
from DreamApp import models
from Dream import settings
import sweetify
from django.template.loader import render_to_string
from datetime import datetime
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _

# Create your views here.
def home(request):
    services = models.Service.objects.all()
    info = models.Info_extra.objects.all()
    sponsor = models.Sponsor.objects.all()
    blog = models.Blog.objects.order_by("-id").all()[:3]
    return render(request, 'inicio.html', {'services': services, 'info': info, 'blog': blog, 'sponsor': sponsor, })

def services(request):
    services = models.Service.objects.all()
    planes = models.Planes.objects.all()
    return render(request, 'services.html', {'services': services, 'planes': planes})


def blog(request, index):
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
    return render(request, 'blog.html', {'page_obj': page_obj, 'destacado': destacado, })

def blog_detail(request, id):
    blog = models.Blog.objects.filter(id=id)
    blogs = models.Blog.objects.exclude(id=id).order_by("-id").all()[:3]
    destacado = models.Blog.objects.filter(active=True).all()
    return render(request, 'blog_details.html',
                  {'blog': blog.get(),'destacado': destacado, 'blogs': blogs})

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
        message = render_to_string('correo_contact.html', {
            'mensaje': comentario,
        })
        send_mail(subject,
                  message,
                  settings.EMAIL_HOST_USER,
                  [entidad.email]  # destinatario
                  )
        sweetify.success(request, 'Mensaje enviado con éxito', button='Ok', timer=5000)
        return HttpResponseRedirect("/contact/")
    return render(request, "contact.html")

def team(request):
    team = models.Team.objects.all()
    return render(request, 'team.html', {'team': team})
