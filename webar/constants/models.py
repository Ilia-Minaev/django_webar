from django.db import models
from django.utils.safestring import mark_safe



class Constants(models.Model):
    site_name = models.CharField(max_length=256, blank=True, verbose_name='site name')
    address = models.CharField(max_length=256, blank=True, verbose_name='address')
    #logo = models.ImageField()
    email = models.EmailField(blank=True, verbose_name='email')
    phone1 = models.PositiveSmallIntegerField(default=0, verbose_name='phone1')
    phone2 = models.PositiveSmallIntegerField(default=0, verbose_name='phone2')
    facebook = models.CharField(max_length=256, blank=True, verbose_name='facebook')
    twitter = models.CharField(max_length=256, blank=True, verbose_name='twitter')
    instagram = models.CharField(max_length=256, blank=True, verbose_name='instagram')
    linkedin = models.CharField(max_length=256, blank=True, verbose_name='linkedin')
    youtube = models.CharField(max_length=256, blank=True, verbose_name='youtube')
    vk = models.CharField(max_length=256, blank=True, verbose_name='vk')

    def __str__(self):
        return self.site_name
    
    class Meta:
        verbose_name = 'Constant'
        verbose_name_plural = 'Constants'

class Slider(models.Model):
    action = models.BooleanField(default=True)
    title = models.CharField(max_length=128, blank=False, verbose_name='title')
    description = models.TextField(max_length=512, blank=True, verbose_name='description')
    image = models.ImageField(upload_to='uploads/slider/', blank=True, verbose_name='image')
    button_title = models.CharField(max_length=64, blank=True, verbose_name='button title')
    button_slug = models.CharField(max_length=256, blank=True, verbose_name='button slug')

    def __str__(self) -> str:
        return self.title
    
    def show_img(self):
        if self.image:
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100" height="100"></a>'.format(self.image.url))
        else:
            return '<div>No photo</div>'
        
    show_img.short_description = 'Image'
    show_img.allow_tags = True
    
    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'