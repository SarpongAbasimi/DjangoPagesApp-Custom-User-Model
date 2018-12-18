from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Articles(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    time =models.DateField(auto_now_add=True)
    author=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
     
     """ This enusres that the Atticle models doesn't have to end with another s """
    class Meta:
        verbose_name_plural='Articles'

    def __str__(self):
        return self.title

    """ This is to tell django how to find the url of the Article model object """
    def get_absolute_url(self):
        return reverse('article_detail',args=([str(self.id)]))




