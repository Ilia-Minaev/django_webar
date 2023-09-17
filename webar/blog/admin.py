from django.contrib import admin

from blog.models import Page, Articles

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_updated')
    list_display_links = ('title',)
    readonly_fields = ('date_created', 'date_updated')
    prepopulated_fields = {'slug': ('title',)}

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('action', 'title', 'show_img')
    list_display_links = ('title',)
    fields = ('action', 'title', 'slug', 'show_img', 'image', 'description', 'meta_title',
              'meta_keywords', 'meta_description', 'date_created', 'date_updated')
    readonly_fields = ('show_img', 'date_created', 'date_updated')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Page, PageAdmin)
admin.site.register(Articles, ArticlesAdmin)