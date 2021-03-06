from django.db import models

# Create your models here.

class Movie(models.Model):
    movie_id = models.CharField(max_length=200, primary_key=True, unique=True)
    movie_title = models.CharField(max_length=200)
    movie_simple_describe = models.CharField(max_length=200)
    movie_detailed_describe = models.TextField()
    movie_link = models.URLField()
    movie_review_link = models.URLField(default="")
    movie_published = models.CharField(max_length=10)

    def __str__(self):
        return self.movie_title