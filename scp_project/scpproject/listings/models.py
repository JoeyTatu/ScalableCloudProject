from django.db import models

# Create your models here.
class Listing(models.Model):
    address = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    
    property_class = models.CharField(max_length=20) # house, flat, apt, etc
    property_type = models.CharField(max_length=20) # semi-detached, terrace, etc
    description = models.CharField(max_length=5000, default="0")
    features = models.CharField(max_length=5000, default="0")
    
    no_bedrooms = models.IntegerField()
    no_bathrooms = models.IntegerField()
    ber_rating = models.CharField(max_length=2, default="A1")
    
    photo1 = models.FileField(upload_to="media/")
    photo2 = models.FileField(upload_to="media/")
    photo3 = models.FileField(upload_to="media/")
    photo4 = models.FileField(upload_to="media/")
    photo5 = models.FileField(upload_to="media/")
    
    contact_name = models.CharField(max_length=50, default="none")
    contact_email = models.EmailField(max_length=50, default="none")
    contact_phone = models.CharField(max_length=50, default="none")
    
    date_added = models.DateField('date_added')
    
    def __str__(self):
        return self.address + " - " + self.price
    
    
    
