from django.contrib import admin

from constants.models import Constants
from constants.forms import PhoneAdminForm

class ConstantsAdmin(admin.ModelAdmin):
    list_display = ('site_name',)
    list_display_links = ('site_name',)

    form = PhoneAdminForm

    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(Constants, ConstantsAdmin)