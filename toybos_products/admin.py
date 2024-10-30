from django.contrib import admin
from django.utils.html import format_html
from solo.admin import SingletonModelAdmin
from modeltranslation.admin import TranslationAdmin

from toybos_products.models import Category, Product, Publication, AboutMe, Recipes, SocialMediaContact


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    """Категория для продукта"""
    list_display = ['name']


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    """Продукты """
    list_display = ['name', 'category', 'product_image_tag']

    def product_image_tag(self, obj):
        return format_html('<img src="{}"  height="80" />'.format(obj.image.url))


@admin.register(Publication)
class PublicationAdmin(TranslationAdmin):
    """Публикация"""
    list_display = ['title', 'publication_image_tag']

    def publication_image_tag(self, obj):
        return format_html('<img src="{}"  height="60" width=70 />'.format(obj.image.url))


class AboutMeAdmin(TranslationAdmin, SingletonModelAdmin):
    pass


admin.site.register(AboutMe, AboutMeAdmin)

admin.site.register(SocialMediaContact, SingletonModelAdmin)


@admin.register(Recipes)
class RecipesAdmin(TranslationAdmin):
    """Рецепты"""
    list_display = ['title', 'recipes_image_tag']

    def recipes_image_tag(self, obj):
        return format_html('<img src="{}"  height="60" width=70 />'.format(obj.image.url))

