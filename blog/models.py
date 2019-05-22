from django.db import models

# Create your models here.


class PostForms(models.Model):
    title = models.CharField(max_length = 140)
    name = models.CharField(max_length = 140)
    ls = models.TextField()
    question = models.TextField()
    presentation = models.TextField()
    background = models.TextField()
    perfTask = models.TextField()
    quiz = models.TextField()
    vocab = models.TextField()
    wiki =models.TextField()

    def __str__(self):
        return self.title
