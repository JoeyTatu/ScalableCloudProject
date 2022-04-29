from django.db import models

# Create your models here.
class Listing(models.Model):
    address = models.CharField(max_length=100)
    price = models.IntegerField()
    
    property_class = models.CharField(max_length=20) # house, flat, apt, etc
    property_type = models.CharField(max_length=20) # semi-detached, terrace, etc
    description = models.CharField(max_length=1000)
    features = models.CharField(max_length=500)
    
    no_bedrooms = models.IntegerField()
    no_bathrooms = models.IntegerField()
    ber_rating = models.CharField(max_length=2)
    
    property_map = models.CharField(max_length=100)
    photos = models.CharField(max_length=100)
    date_added = models.DateTimeField('date added')
    
    contact_name = models.CharField(max_length=50, default='null')
    contact_email = models.EmailField(max_length=50, default='null')
    contact_phone = models.CharField(max_length=50, default='null')
    
    def __str__(self):
        return self.address + " - " + self.price
    
    
    
