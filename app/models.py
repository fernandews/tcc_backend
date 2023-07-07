from django.db import models
from django.contrib.gis.db import models

from django.contrib.auth.models import AbstractUser

TYPE_CHOICES = (
    ('visually_impaired', 'Deficiente visual'),
    ('limited_mobility', 'Dificldades de locomoção'), 
    ('control_group', 'Grupo de controle')
)
PATH_CHOICES = (
    ('shorter', 'Caminho mais curto'),
    ('lighter', 'Caminho mais iluminado'), 
    ('most_uniform', 'Caminho mais uniforme'),
    ('social', 'Caminho com amigos')
)
BUILDING_CHOICES = (
    ('arquitetura', 'Inserir coordenadas aqui'),
)

class User(AbstractUser):
    name = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    birthdate = models.CharField(max_length=255)
    user_type = models.CharField(max_length=255, choices=TYPE_CHOICES)
    choses_path_by = models.CharField(max_length=255, choices=PATH_CHOICES)
    goes_to = models.CharField(max_length=255, choices=BUILDING_CHOICES)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    
class Geolocation(models.Model):
    user = models.IntegerField()
    occurrence_datetime = models.DateTimeField()
    geolocation_data = models.LineStringField()

    def __str__(self):
        return f'ID: {self.user}, Data/Hora: {self.occurrence_datetime}'