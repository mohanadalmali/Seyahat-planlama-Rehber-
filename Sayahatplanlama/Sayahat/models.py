from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="media")
    show_on_homepage = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class ServiceDetail(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="media")
    description = models.TextField()
    link1_title = models.CharField(max_length=100, blank=True)
    link1_url = models.URLField(blank=True)
    link2_title = models.CharField(max_length=100, blank=True)
    link2_url = models.URLField(blank=True)
    
    main_title1 = models.CharField(max_length=200)
    title1 = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to="media")
    description1 = models.TextField()
    
    
    main_title2 = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)
    image2 = models.ImageField(upload_to="media")
    description2 = models.TextField()
    
    def __str__(self):
        return self.title
