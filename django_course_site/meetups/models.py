from django.db import models
# from django.db.models.base import Model

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.address})'

class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField() # this is for organizer email
    date = models.DateField() 
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE) # this is an one to many case
    Participants = models.ManyToManyField(Participant, blank=True, null=True) # this is a many to many case

    def __str__(self):
        return f'{self.title} - {self.slug}'
