from django.db import models

# Create your models here.
class Listing(models.Model):
    address = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    
    property_class = models.CharField(max_length=20) # house, flat, apt, etc
    property_type = models.CharField(max_length=20) # semi-detached, terrace, etc
    description = models.CharField(max_length=1000, null=True)
    features = models.CharField(max_length=500, null=True)
    
    no_bedrooms = models.IntegerField()
    no_bathrooms = models.IntegerField()
    ber_rating = models.CharField(max_length=2, null=True)
    property_map = models.CharField(max_length=100, null=True)
    
    photo1 = models.FileField(upload_to="media/", null=True)
    photo2 = models.FileField(upload_to="media/", null=True)
    photo3 = models.FileField(upload_to="media/", null=True)
    photo4 = models.FileField(upload_to="media/", null=True)
    photo5 = models.FileField(upload_to="media/", null=True)
    
    contact_name = models.CharField(max_length=50, null=True)
    contact_email = models.EmailField(max_length=50, null=True)
    contact_phone = models.CharField(max_length=50, null=True)
    
    date_added = models.DateField('date_added')
    
    def __str__(self):
        return self.address + " - " + self.price
    
    
    
