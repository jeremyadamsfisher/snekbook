from django.db import models

class Snake(models.Model):
    genus = models.CharField(max_length=200)
    species = models.CharField(max_length=200)
    fangs = models.CharField(max_length=200)
    toxicity = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)
    common_name = models.CharField(max_length=200)
    recommended_snakes = models.ManyToManyField('self')

    def __str__(self):
        return " ".join((self.genus, self.species))
