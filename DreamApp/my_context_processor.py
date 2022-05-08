from DreamApp import models
import datetime
x = datetime.datetime.now()


def general(context):
    y = x.year
    general = models.General.objects.first()
    sponsor = models.Sponsor.objects.all()
    return {'general': general,
            'sponsor': sponsor,
            'x': y,
            }

