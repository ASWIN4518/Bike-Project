from django.db import models


class Brand(models.Model):
    name=models.CharField(max_length=100)
    country=models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Bike(models.Model):
    bike_name=models.CharField(max_length=200)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,related_name="bikes",null=True,
    blank=True)
    brand_name=models.CharField(max_length=100)
    Price=models.DecimalField(max_digits=10,decimal_places=2)
    Engine_capacity=models.IntegerField()
    Mileage=models.DecimalField(max_digits=5 , decimal_places=2)
    Fuel_type=models.CharField(max_length=200)
    Description=models.TextField()

    def __str__(self):
        return self.bike_name

      

   

