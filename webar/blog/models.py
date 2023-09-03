from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    #def _(str):
        #pass
    #title = models.CharField(_("dd"), max_length=128)
    title = models.CharField(max_length=128, blank=False, verbose_name='title')
    slug = models.SlugField(max_length=256, unique=True, verbose_name='url')
    description = models.TextField(blank=True, verbose_name='description')
    meta_title = models.CharField(max_length=128, blank=True, verbose_name='m_title')
    meta_keywords = models.CharField(max_length=128, blank=True, verbose_name='m_keywords')
    meta_description = models.CharField(max_length=128, blank=True, verbose_name='m_description')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Create date')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Update date')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

