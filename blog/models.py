from django.db import models

# Create your models here.
class Blog (models.Model):
    title = models.CharField(max_length=100)
    Date = models.DateField (auto_now="True")
    description = models.CharField(max_length = 250)
    url = models.URLField(blank="True")

    def __str__(self):
        return self.title