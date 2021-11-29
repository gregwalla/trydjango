from django.db import models
from django.urls import reverse



# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank = True, null= True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    summary = models.TextField(blank = True, null= True)
    featured = models.BooleanField(null = True, default = True)

    def get_absolute_url(self): #convention to grab the url 
        return reverse("blog:article-detail", kwargs={"id": self.id} )