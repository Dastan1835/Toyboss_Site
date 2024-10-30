from django.core.paginator import Paginator
from django.http import Http404
from django.views.generic import TemplateView
from .models import Category, Product, Publication, AboutMe, Recipes, SocialMediaContact


class ProductView(TemplateView):
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = {
            'products': Category.objects.prefetch_related('products').all(),
            'social_media': SocialMediaContact.objects.first()
        }
        return context


class ProductDetailView(TemplateView):
    template_name = 'product-inner.html'

    def get_context_data(self, **kwargs):
        product_pk = kwargs['pk']
        try:
            product = Product.objects.get(id=product_pk)
        except Product.DoesNotExist:
            raise Http404
        product_category = product.category
        context = {
            'product': product,
            'similar_products': Product.objects.filter(category=product_category).exclude(id=product_pk).distinct(),
            'social_media': SocialMediaContact.objects.first()
        }
        return context


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        last_two_publications = Publication.objects.order_by('-id')[:2]
        context = {
            'about_me': AboutMe.objects.first(),
            'publications': last_two_publications,
            'social_media': SocialMediaContact.objects.first()
        }
        return context


class AboutView(TemplateView):
    template_name = 'about-company.html'

    def get_context_data(self, **kwargs):

        context = {
            'about_me': AboutMe.objects.first(),
            'social_media': SocialMediaContact.objects.first()
        }
        return context


class PublicationsView(TemplateView):
    template_name = 'publications.html'

    def get_context_data(self, **kwargs):
        publications = Publication.objects.filter(is_active=True)
        paginator = Paginator(publications, 2)
        page_number = self.request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
            'social_media': SocialMediaContact.objects.first()
        }
        return context


class PublicationsInnerView(TemplateView):
    template_name = 'publications-inner.html'

    def get_context_data(self, **kwargs):
        publication_pk = kwargs['pk']
        try:
            publication = Publication.objects.get(id=publication_pk)
        except Publication.DoesNotExist:
            raise Http404
        context = {
            'publication': publication,
            'social_media': SocialMediaContact.objects.first()
        }
        return context


class RecipesView(TemplateView):
    template_name = 'recipes.html'

    def get_context_data(self, **kwargs):
        publications = Recipes.objects.filter(is_active=True)
        paginator = Paginator(publications, 2)
        page_number = self.request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
            'social_media': SocialMediaContact.objects.first()
        }
        return context


class RecipesInnerView(TemplateView):
    template_name = 'recipes-inner.html'

    def get_context_data(self, **kwargs):
        recipes_pk = kwargs['pk']
        try:
            recipes = Recipes.objects.get(id=recipes_pk)
        except Recipes.DoesNotExist:
            raise Http404
        context = {
            'recipes': recipes,
            'social_media': SocialMediaContact.objects.first()
        }
        return context

