from django.core.validators import MinLengthValidator
from django.db import models
from ckeditor.fields import RichTextField
from solo.models import SingletonModel


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Категория"
        verbose_name = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(null=True)
    ingredients = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Продукт"
        verbose_name = "Продукты"

    def __str__(self):
        return self.name


class Publication(models.Model):
    title = models.CharField(max_length=250, default='колбаса')
    created_at = models.DateField(auto_now_add=True, null=True)
    short_description = models.CharField(null=True, max_length=250)
    description = models.TextField(default="хорошоя колбаса")
    image = models.ImageField(default="/media/post-5_A8VoxH3.jpeg/")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Публикация"
        verbose_name = "Публикации"


class AboutMe(SingletonModel):
    title = models.CharField(max_length=250, null=True)
    short_description = models.TextField(max_length=400, null=True)
    image = models.ImageField(null=True)
    description = RichTextField()

    class Meta:
        verbose_name_plural = "О нас"
        verbose_name = "О нас "


class SocialMediaContact(SingletonModel):
    instagram = models.URLField()
    facebook = models.URLField()
    phone_number = models.CharField(max_length=20, validators=[MinLengthValidator(7)])

    class Meta:
        verbose_name_plural = "Социальные сети и контакт"
        verbose_name = "Социальные сети и контакт"


class Recipes(models.Model):
    title = models.CharField(max_length=250, null=True)
    description = models.TextField()
    image = models.ImageField()
    ingredients = RichTextField(null=True)
    directions = RichTextField(null=True)
    products = models.ManyToManyField(Product, related_name='recipes')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Рецепт"
        verbose_name = "Рецепты "