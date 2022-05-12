from django.contrib import admin
from DreamApp.models import *
# Register your models here.

class AdminGeneral(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    list_filter = ["name"]
    fieldsets = (
        ('Textos dinámicas', {
            'fields': (
                'name', 'slogan_1', 'slogan_2', 'slogan_3', 'text_1_solicitud', 'text_2_solicitud', 'text_3_solicitud',
                'text_portafolio_inicio',
                'text_1_about', 'descripcion_about')
        }),
        ('Fotos dinámicas', {
            'fields': ('image_banner_1', 'image_banner_2', 'image_about')
        }),
        ('Información de Contactos', {
            'fields': ('address', 'email', 'horario', 'map_addres', 'phone',
                       'face', 'inst', 'twit', 'yout', 'link')
        }),
    )

    class Meta:
        model = General


admin.site.register(General, AdminGeneral)


class AdminBlog(admin.ModelAdmin):
    list_display = ["title", 'active', "created_at"]
    list_display_links = ["title"]
    list_filter = ["title"]
    list_editable = ["active"]
    list_per_page = 10

    class Meta:
        model = Blog

admin.site.register(Blog, AdminBlog)


class AdminGaleryBlog(admin.ModelAdmin):
    list_display = ["blog"]
    list_display_links = ["blog"]
    list_filter = ["blog"]
    list_per_page = 10

    class Meta:
        model = Galery_blog


admin.site.register(Galery_blog, AdminGaleryBlog)

class AdminInfExtra(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ["title"]
    list_filter = ['title']
    list_per_page = 10

    class Meta:
        model = Info_extra


admin.site.register(Info_extra, AdminInfExtra)

class AdminSponsor(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ["name"]
    list_filter = ['name']
    list_per_page = 10

    class Meta:
        model = Sponsor


admin.site.register(Sponsor, AdminSponsor)


class AdminServices(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ["name"]
    list_filter = ['name']
    list_per_page = 10

    class Meta:
        model = Service


admin.site.register(Service, AdminServices)

class AdminMoneda(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    list_filter = ["name"]
    list_per_page = 5

    class Meta:
        model = Moneda

admin.site.register(Moneda, AdminMoneda)


class AdminPlan(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    list_filter = ["name"]
    list_per_page = 5

    class Meta:
        model = Planes

admin.site.register(Planes, AdminPlan)


class AdminTipoGalery(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    list_filter = ["name"]
    list_per_page = 5

    class Meta:
        model = Tipo_galery

admin.site.register(Tipo_galery, AdminTipoGalery)


class AdminGalery(admin.ModelAdmin):
    list_display = ["title", 'active']
    list_display_links = ["title"]
    list_filter = ["title"]
    list_editable = ["active"]
    list_per_page = 5

    class Meta:
        model = Galery

admin.site.register(Galery, AdminGalery)


class AdminSolicitud(admin.ModelAdmin):
    list_display = ['full_name', 'servicio', 'phone', "created_at"]
    list_display_links = ["full_name", 'phone']
    list_filter = ['phone', 'full_name']
    list_per_page = 10

    class Meta:
        model = Solicitud

admin.site.register(Solicitud, AdminSolicitud)

class AdminTeam(admin.ModelAdmin):
    list_display = ["name", "ocupation"]
    list_display_links = ["name", "ocupation"]
    list_filter = ["name", "ocupation"]
    list_per_page = 5

    class Meta:
        model = Team

admin.site.register(Team, AdminTeam)


class AdminOpinion(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    list_filter = ["name"]
    list_per_page = 5

    class Meta:
        model = Opinion

admin.site.register(Opinion, AdminOpinion)

class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", 'email', "created_at"]
    list_display_links = ["name", 'email']
    list_filter = ['email']
    list_per_page = 10

    class Meta:
        model = Contact
admin.site.register(Contact, ContactAdmin)
