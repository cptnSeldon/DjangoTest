from django.db import models

# Create your models here.

# TODO-01 create models then makemigrations + migrate
class Post(models.Model):
    text = models.TextField()

    # TODO-03 add string representation to the model
    def __str__(self):
        """ string representation of the model """
        return self.text[:50]
