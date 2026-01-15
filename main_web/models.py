from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_name = models.CharField(max_length=50, help_text="FontAwesome class or image path")
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.title

class Project(models.Model):
    client_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/')
    description = models.TextField()

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    client_logo = models.ImageField(upload_to='clients/')
    client_name = models.CharField(max_length=100)
    quote = models.TextField()
    
    def __str__(self):
        return self.client_name