from django import forms

from blog.models import Page, Articles

from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PageAdminForm(forms.ModelForm):
    description = forms.CharField(label='Description', widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Page
        fields = '__all__'

class ArticlesAdminForm(forms.ModelForm):
    description = forms.CharField(label='Description', widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Articles
        fields = '__all__'