from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)
    mfg = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=7)  # allows for prices up to 99999.99
    image = models.URLField()

    def __unicode__(self):
        return self.name
