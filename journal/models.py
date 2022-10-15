from django.db import models


class Journal(models.Model):
    title = models.CharField(max_length=128, blank=False)
    description = models.TextField()
    date_of_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_of_create']

    def __str__(self):
        return self.title
