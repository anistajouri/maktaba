from django.db import models
    
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)

    quantity = models.IntegerField(default=1)
    product = models.CharField(max_length=30)
    price_achat = models.FloatField(default=0.0)    
    price_vente = models.FloatField(default=0.0)
    remise = models.FloatField(default=0.0) 
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
	    return self.name