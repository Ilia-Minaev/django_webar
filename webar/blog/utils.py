from blog.models import Page
from constants.models import Constants


class DataMixin:
    def get_user_base_context(self, **kwargs):
        context = kwargs
        page = Page.objects.get(slug=self.kwargs['slug'])
        constants = Constants.objects.get(pk=1)
        context['title'] = page.title
        context['description'] = page.description
        context['meta_title'] = page.meta_title or page.title
        context['meta_description'] = page.meta_description
        context['meta_keywords'] = page.meta_keywords

        context['site_name'] = constants.site_name or False
        context['address'] = constants.address or False
        #context['logo'] = constants.logo or False
        context['email'] = constants.email or False
        context['phone1'] = constants.phone1 or False
        context['phone2'] = constants.phone2 or False
        context['facebook'] = constants.facebook or False
        context['twitter'] = constants.twitter or False
        context['instagram'] = constants.instagram or False
        context['linkedin'] = constants.linkedin or False
        context['youtube'] = constants.youtube or False
        context['vk'] = constants.vk or False

        return context