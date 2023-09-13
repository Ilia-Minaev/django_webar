from django.db import models



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
