from modeltranslation.translator import register, TranslationOptions
from .models import Category, Product, Publication, AboutMe, Recipes


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Product)
class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'ingredients')


@register(Publication)
class PublicationCategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description')


@register(AboutMe)
class AboutMeTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description')


@register(Recipes)
class RecipesTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'ingredients', 'directions')