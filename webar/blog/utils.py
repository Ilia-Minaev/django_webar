from blog.models import Page


class DataMixin:
    def get_user_base_context(self, **kwargs):
        context = kwargs
        page = Page.objects.get(slug=self.kwargs['slug'])
        context['title'] = page.title
        context['description'] = page.description
        context['meta_title'] = page.meta_title or page.title
        context['meta_description'] = page.meta_description
        context['meta_keywords'] = page.meta_keywords
        return context