from django.db import models

class Post(models.Model):
    genus = models.TextField()
    species = models.TextField()
    fangs = models.TextField()
    toxicity = models.TextField()
    rating = models.TextField()
    common_name = models.TextField()
    recommended_snakes = models.TextField()

    def __str__(self):
        return " ".join((self.genus, self.species))
