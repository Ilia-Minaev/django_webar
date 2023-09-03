from django.contrib import admin

from blog.models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_updated')
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('date_created', 'date_updated')

admin.site.register(Page, PageAdmin)