from django.db import models

# Create your models here.


class TwitterData(models.Model):
    created = models.DateField()
    post_id = models.CharField(max_length=64, unique=True)
    text = models.CharField(max_length=256, blank=False)
    location = models.CharField(max_length=32)

    def __str__(self):
        return self.post_id + " " + unicode(self.created)
