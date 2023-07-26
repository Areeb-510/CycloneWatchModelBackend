from django.db import models

# Create your models here.
class CycloneIntensity(models.Model):
    intensity = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.intensity
