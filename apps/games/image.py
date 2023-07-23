from django.db import models
from games.models import Game 

class Image(models.Model):

    game = models.ForeignKey(
        to=Game,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(
        verbose_name='изображение',
        upload_to='games/',
        default='games/unknown.png'
    )