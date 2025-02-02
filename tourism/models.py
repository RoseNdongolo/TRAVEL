from django.db import models


from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from django.db import models

class Destination(models.Model):
    CATEGORY_CHOICES = [
        
        ('Forest', 'Forest'),
        ('Attraction', 'Attraction'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations/', null=True, blank=True)
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=True,blank=True)

    def __str__(self):
        return self.name


class Attraction(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='attractions/', null=True, blank=True) 
    location = models.CharField(max_length=100)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Review(models.Model):
    rating = models.IntegerField()
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Booking(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, null=True, blank=True)
    booking_date = models.DateField()
    num_guests = models.IntegerField()
    username = models.CharField(max_length=150, null=True)  
    email = models.EmailField(null=True, blank=True)  
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')],
        help_text="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", null=True
    )  

    def __str__(self):
        return f"{self.username} - {self.destination}"


