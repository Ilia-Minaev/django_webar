from django.db import models
from django.urls import reverse


"""
class GeneralConstants(models.Model):
    site_name = models.CharField(max_length=256, verbose_name='site name')
    #logo = models.ImageField()
    email = models.EmailField(verbose_name='email')
    phone1 = models.PositiveIntegerField(verbose_name='phone1')
    phone2 = models.PositiveIntegerField(verbose_name='phone2')
    facebook = models.CharField(max_length=256, verbose_name='facebook')
    twitter = models.CharField(max_length=256, verbose_name='twitter')
    instagram = models.CharField(max_length=256, verbose_name='instagram')
    linkedin = models.CharField(max_length=256, verbose_name='linkedin')
    youtube = models.CharField(max_length=256, verbose_name='youtube')
    vk = models.CharField(max_length=256, verbose_name='vk')
    address = models.CharField(max_length=256, verbose_name='address')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
"""
class Page(models.Model):
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
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

