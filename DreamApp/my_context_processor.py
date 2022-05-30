from DreamApp import models, forms
import datetime
x = datetime.datetime.now()


def general(context):
    y = x.year
    solicitud = models.Solicitud.objects.all()
    general = models.General.objects.first()
    form = forms.SolicitudForm()
    sponsor = models.Sponsor.objects.all()
    return {'general': general,
            'solicitud': solicitud,
            'sponsor': sponsor,
            'form': form,
            'x': y,
            }

# // toLowerCase().replace(/\s/g,"-"); .split("").slice(-1)[0];