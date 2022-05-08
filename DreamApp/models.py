from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class General(models.Model):
    created_at = models.DateTimeField(verbose_name="Creado", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modificado")
    name = models.CharField(max_length=255,help_text="Nombre del negocio", verbose_name="Nombre")
    slogan_1 = models.CharField(max_length=255, verbose_name="Texto del Banner Inicio 1", help_text="Primer texto en la imagen del banner en la Página de inicio", blank=True, null=True)
    slogan_2 = models.CharField(max_length=255, verbose_name="Texto del Banner Inicio 2",help_text="Segundo texto en la imagen del banner de inicio", blank=True, null=True)
    slogan_3 = models.CharField(max_length=255, verbose_name="Texto del Banner Inicio 3",help_text="Tercer Texto en la imagen del banner de inicio", blank=True, null=True)
    text_1_solicitud = models.CharField(max_length=255, verbose_name="Primer texto de formulario solicitud",help_text="1er texto del Cartel arriba del formulario", blank=True, null=True)
    text_2_solicitud = models.CharField(max_length=255, verbose_name="Segundo texto de formulario solicitud",help_text="2do texto del Cartel arriba del formulario", blank=True, null=True)
    text_3_solicitud = models.CharField(max_length=255, verbose_name="Tercer texto de formulario solicitud",help_text="3er texto del Cartel arriba del formulario", blank=True, null=True)
    text_portafolio_inicio = models.CharField(max_length=255, verbose_name="Texto que encabeza el portafolio",help_text="Texto que encabeza el portafolio en inicio", blank=True, null=True)
    image_banner_1 = models.ImageField(upload_to='static/upload', verbose_name="Imagen Banner Inicio",help_text="Imagen del Banner en la Página de inicio")
    text_1_about = models.CharField(max_length=255, verbose_name="Titulo de Contactos",
                                      help_text="Titulo de la página Nosotros", blank=True,
                                      null=True)
    descripcion_about = RichTextField(verbose_name="Descripcion de Nosotros",help_text="Descripción de la Página Nosotros")
    image_about = models.ImageField(upload_to='static/upload', verbose_name="Imagen de nosotros",help_text="Imagen de la página Nosotros")
    image_banner_2 = models.ImageField(upload_to='static/upload', verbose_name="Imagen Banner Otras Vistas",help_text="Imagen del Banner en el resto de las vistas")
    address = models.CharField(max_length=255, verbose_name="Direccion", blank=True, null=True)
    horario = models.CharField(max_length=255, verbose_name="Horarios",help_text="Horarios", blank=True, null=True)
    email = models.EmailField(verbose_name="Correo de Contactos", blank=True, null=True,help_text="Correo que aparece en la página contactos")
    map_addres = models.TextField(verbose_name="Direccion google maps, src", help_text="Mapa de la ubicación del negocio")
    phone = models.CharField(max_length=255, verbose_name="Telefono")
    face = models.URLField(verbose_name="Facebook",  blank=True, null=True)
    inst = models.URLField(verbose_name="Instagram", blank=True, null=True)
    twit = models.URLField(verbose_name="Twitter",  blank=True, null=True)
    yout = models.URLField(verbose_name="YouTube", blank=True, null=True)
    link = models.URLField(verbose_name="Linkedin", blank=True, null=True)

    class Meta:
        verbose_name_plural = "A. General"

    def __str__(self):
        return str(self.name)



class Blog(models.Model):
    created_at = models.DateField(verbose_name="Creado", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modificado")
    title = models.CharField(max_length=255, verbose_name="Título")
    text_small = models.CharField(max_length=255, verbose_name="Texto pequeño", blank=True, null=True)
    descripcion = RichTextField(verbose_name="Descripción")
    active = models.BooleanField(verbose_name="Destacado", default=False)
    image = models.ImageField(upload_to="static/upload", verbose_name="Imagen Principal", null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "B. Blog"

class Galery_blog(models.Model):
    created_at = models.DateField(verbose_name="Creado", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modificado")
    image = models.ImageField(upload_to="static/upload", verbose_name="Imagen", null=True)
    blog = models.ForeignKey(Blog, models.CASCADE, verbose_name="Blog", null=True)

    def __str__(self):
        return self.blog.title

    class Meta:
        verbose_name_plural = "C. Galería del Blog"

class Info_extra(models.Model):
    created_at = models.DateField(verbose_name="Creado", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modificado")
    title = models.CharField(max_length=255, verbose_name="Título")
    cantidad = models.IntegerField(verbose_name="Cantidad", blank=True, null=True)
    image = models.ImageField(upload_to="static/upload", verbose_name="Logo", null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "D. Información Extra"

class Sponsor(models.Model):
    created_at = models.DateField(verbose_name="Creado", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modificado")
    name = models.CharField(max_length=255, verbose_name="Nombre")
    image = models.ImageField(upload_to="static/upload", verbose_name="Logo", null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "E. Patrocinadores"

class Moneda(models.Model):
    created_at = models.DateTimeField(verbose_name="Creado", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modificado")
    name = models.CharField(max_length=255, verbose_name="Tipo de Moneda")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "F. Tipos de Monedas"

class Planes(models.Model):
    created_at = models.DateField(verbose_name="Creado", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modificado")
    name = models.CharField(max_length=255, verbose_name="Nombre")
    moneda = models.ForeignKey(Moneda, models.CASCADE, verbose_name="Tipo de Moneda")
    price = models.FloatField(default=0, verbose_name="Precio del plan")
    descripcion = RichTextField(verbose_name="Descripción", default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "G. Planes de boda"


class Tipo_galery(models.Model):
    created_at = models.DateField(verbose_name="Creado", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modificado")
    name = models.CharField(max_length=255, verbose_name="Nombre")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "H. Tipo de Galería"

class Galery(models.Model):
    created_at = models.DateField(verbose_name="Creado", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modificado")
    title = models.CharField(max_length=255, verbose_name="Título")
    text = models.CharField(max_length=255, verbose_name="Texto")
    image = models.ImageField(upload_to="static/upload", verbose_name="Imagen", null=True)
    tipo = models.ForeignKey(Tipo_galery, models.CASCADE, verbose_name="Tipo de Galería")


    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "I. Galería"

class Solicitud(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created_at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated_at")
    email = models.EmailField(max_length=255,verbose_name="Email")
    phone = models.CharField(max_length=255, verbose_name="Teléfono", default='')
    full_name = models.CharField(max_length=255, verbose_name="Nombre Completo")
    tipo_servicio = models.CharField(max_length=255, verbose_name="Tipo de Servicio")
    text = models.TextField(verbose_name="Mensaje")
    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "J. Solicitudes"

class Service(models.Model):
    created_at = models.DateField(verbose_name="Creado", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modificado")
    name = models.CharField(max_length=255, verbose_name="Nombre del servicio")
    text = RichTextField(verbose_name="Texto")
    image = models.ImageField(upload_to="static/upload", verbose_name="Imagen", null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "K. Servicios"


class Team(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created_at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated_at")
    name = models.CharField(max_length=255, verbose_name="Nombre Completo")
    ocupation = models.CharField(max_length=255, verbose_name="Ocupación")
    image = models.ImageField(upload_to="static/upload", verbose_name="Imagen", null=True)
    face = models.URLField(verbose_name="Facebook", blank=True, null=True)
    inst = models.URLField(verbose_name="Instagram", blank=True, null=True)
    twit = models.URLField(verbose_name="Twitter", blank=True, null=True)
    link = models.URLField(verbose_name="Linkedin", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "L. Equipo de trabajo"

class Opinion(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created_at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated_at")
    name = models.CharField(max_length=255, verbose_name="Nombre Completo")
    text = models.TextField(verbose_name="Texto")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "M. Opiniones"

class Contact(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated_at")
    name = models.CharField(max_length=255, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Email")
    text = models.TextField(verbose_name="Mensaje")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "N. Contactos"
