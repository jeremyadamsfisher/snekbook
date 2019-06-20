import django.contrib.auth as dj_auth
import django.db.models as models


class Snake(models.Model):
    list_display = ("genus", "species")
    genus = models.CharField(max_length=200)
    species = models.CharField(max_length=200)
    fangs = models.CharField(max_length=200)
    toxicity = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)
    common_name = models.CharField(max_length=200)
    img_thumb = models.CharField(max_length=20)
    img_norm = models.CharField(max_length=20)
    recommended_snakes = models.ManyToManyField("self")
    likers = models.ManyToManyField(dj_auth.get_user_model())

    def __str__(self):
        return " ".join((self.genus, self.species))


class Comment(models.Model):
    list_display = ("text",)
    snake = models.ForeignKey(Snake, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(dj_auth.get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "{}: {}".format(self.author, self.text)
