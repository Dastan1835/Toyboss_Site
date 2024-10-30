from django.test import TestCase
from toybos_products.models import Product, Category, Publication, Recipes
from django.urls import reverse
from .models import Recipes, SocialMediaContact


class HomeTestCase(TestCase):
    def test_home_ru_success(self):
        response = self.client.get('/ru/home/')
        self.assertEqual(response.status_code, 200)

    def test_home_en_success(self):
        response = self.client.get('/en/home/')

        self.assertEqual(response.status_code, 200)

    def test_home_ky_success(self):
        response = self.client.get('/ky/home/')
        self.assertEqual(response.status_code, 200)

    def test_home_kk_success(self):
        response = self.client.get('/kk/home/')
        self.assertEqual(response.status_code, 200)


class AboutTestCase(TestCase):
    def test_about_en_success(self):
        response = self.client.get('/en/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_ru_success(self):
        response = self.client.get('/ru/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_ky_success(self):
        response = self.client.get('/ky/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_kk_success(self):
        response = self.client.get('/kk/about/')
        self.assertEqual(response.status_code, 200)


class ProductListTestCase(TestCase):

    def test_products_ru_success(self):
        response = self.client.get('/ru/products/')
        self.assertEqual(response.status_code, 200)

    def test_products_en_success(self):
        response = self.client.get('/en/products/')
        self.assertEqual(response.status_code, 200)

    def test_products_ky_success(self):
        response = self.client.get('/ky/products/')
        self.assertEqual(response.status_code, 200)

    def test_products_kk_success(self):
        response = self.client.get('/kk/products/')
        self.assertEqual(response.status_code, 200)


class ProductDetailTestCase(TestCase):

    def test_product_detail_ru_success(self):
        cat_1 = Category.objects.create(name='Полукапчьеная колбаса')
        product = Product.objects.create(
            category=cat_1,
            name="Салями",
            description="хорошая колбаса",
            ingredients="лалалалалалалаалла",
            image="/media/post-5_A8VoxH3.jpeg/"
        )

        response = self.client.get(f'/ru/products/{product.id}/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_en_success(self):
        cat_1 = Category.objects.create(name='Полукапчьеная колбаса')
        product = Product.objects.create(
            category=cat_1,
            name="Салями",
            description="хорошая колбаса",
            ingredients="лалалалалалалаалла",
            image="/media/post-5_A8VoxH3.jpeg/"
        )

        response = self.client.get(f'/en/products/{product.id}/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_ky_success(self):
        cat_1 = Category.objects.create(name='Полукапчьеная колбаса')
        product = Product.objects.create(
            category=cat_1,
            name="Салями",
            description="хорошая колбаса",
            ingredients="лалалалалалалаалла",
            image="/media/post-5_A8VoxH3.jpeg/"
        )

        response = self.client.get(f'/ky/products/{product.id}/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_kk_success(self):
        cat_1 = Category.objects.create(name='Полукапчьеная колбаса')
        product = Product.objects.create(
            category=cat_1,
            name="Салями",
            description="хорошая колбаса",
            ingredients="лалалалалалалаалла",
            image="/media/post-5_A8VoxH3.jpeg/"
        )

        response = self.client.get(f'/kk/products/{product.id}/')
        self.assertEqual(response.status_code, 200)


class PublicationsTestCase(TestCase):
    def setUp(self):
        for i in range(5):
            Publication.objects.create(title=f'Publication {i}', short_description="хорошая колбаса", description="хорошая колбаса" , image="/media/post-5_A8VoxH3.jpeg/")

    def tearDown(self):
        Publication.objects.all().delete()

    def test_publication_ru_success(self):
        response = self.client.get('/ru/publications/')
        self.assertEqual(response.status_code, 200)

    def test_publications_en_success(self):
        response = self.client.get('/en/publications/')
        self.assertEqual(response.status_code, 200)

    def test_publications_ky_success(self):
        response = self.client.get('/ky/publications/')
        self.assertEqual(response.status_code, 200)

    def test_publications_kk_success(self):
        response = self.client.get('/kk/publications/')
        self.assertEqual(response.status_code, 200)


class PublicationsDetailTestCase(TestCase):
    def test_publication_detail_ru_success(self):

        publication = Publication.objects.create(
            title='Товар',
            short_description="хорошая колбаса",
            description="хорошая колбаса",
            image="/media/post-5_A8VoxH3.jpeg/"
        )
        response = self.client.get(f'/ru/publications/{publication.id}/')
        self.assertEqual(response.status_code, 200)

    def test_publication_detail_en_success(self):

        publication = Publication.objects.create(
            title='Товар',
            short_description="хорошая колбаса",
            description="хорошая колбаса",
            image="/media/post-5_A8VoxH3.jpeg/"
        )
        response = self.client.get(f'/en/publications/{publication.id}/')
        self.assertEqual(response.status_code, 200)

    def test_publication_detail_ky_success(self):

        publication = Publication.objects.create(
            title='Товар',
            short_description="хорошая колбаса",
            description="хорошая колбаса",
            image="/media/post-5_A8VoxH3.jpeg/"
        )
        response = self.client.get(f'/ky/publications/{publication.id}/')
        self.assertEqual(response.status_code, 200)

    def test_publication_detail_kk_success(self):

        publication = Publication.objects.create(
            title='Товар',
            short_description="хорошая колбаса",
            description="хорошая колбаса",
            image="/media/post-5_A8VoxH3.jpeg/"
        )
        response = self.client.get(f'/kk/publications/{publication.id}/')
        self.assertEqual(response.status_code, 200)


class RecipesViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name="Sample Category")
        for i in range(15):
            product = Product.objects.create(
                name=f"Sample Product{i}",
                category=category,
                image="media/post-5_A8VoxH3.jpeg/"
            )
            recipe = Recipes.objects.create(
                title=f"Sample Recipe{i}",
                description="Sample description",
                image="media/post-5_A8VoxH3.jpeg/",
                is_active=True
            )
            recipe.products.add(product)

    def test_recipes_ru_status_code(self):

        response = self.client.get('/ru/recipes/')
        self.assertEqual(response.status_code, 200)

    def test_recipes_en_status_code(self):

        response = self.client.get('/en/recipes/')
        self.assertEqual(response.status_code, 200)

    def test_recipes_ky_status_code(self):

        response = self.client.get('/ky/recipes/')
        self.assertEqual(response.status_code, 200)

    def test_recipes_kk_status_code(self):

        response = self.client.get('/kk/recipes/')
        self.assertEqual(response.status_code, 200)


class RecipeDetailViewTest(TestCase):

    def test_recipe_detail_ru_status_code(self):

        category = Category.objects.create(name="Sample Category")
        product = Product.objects.create(
            name="Sample Product",
            category=category,
            image="media/post-5_A8VoxH3.jpeg/"
        )
        recipe = Recipes.objects.create(
            title="Sample Recipe",
            description="Sample description",
            image="media/post-5_A8VoxH3.jpeg/",
            is_active=True
        )
        recipe.products.add(product)

        response = self.client.get(f'/ru/recipes/{recipe.id}/')
        self.assertEqual(response.status_code, 200)

    def test_recipe_detail_en_status_code(self):

        category = Category.objects.create(name="Sample Category")
        product = Product.objects.create(
            name="Sample Product",
            category=category,
            image="media/post-5_A8VoxH3.jpeg/"
        )
        recipe = Recipes.objects.create(
            title="Sample Recipe",
            description="Sample description",
            image="media/post-5_A8VoxH3.jpeg/",
            is_active=True
        )
        recipe.products.add(product)

        response = self.client.get(f'/en/recipes/{recipe.id}/')
        self.assertEqual(response.status_code, 200)

    def test_recipe_detail_ky_status_code(self):

        category = Category.objects.create(name="Sample Category")
        product = Product.objects.create(
            name="Sample Product",
            category=category,
            image="media/post-5_A8VoxH3.jpeg/"
        )
        recipe = Recipes.objects.create(
            title="Sample Recipe",
            description="Sample description",
            image="media/post-5_A8VoxH3.jpeg/",
            is_active=True
        )
        recipe.products.add(product)

        response = self.client.get(f'/ky/recipes/{recipe.id}/')
        self.assertEqual(response.status_code, 200)

    def test_recipe_detail_kk_status_code(self):

        category = Category.objects.create(name="Sample Category")
        product = Product.objects.create(
            name="Sample Product",
            category=category,
            image="media/post-5_A8VoxH3.jpeg/"
        )
        recipe = Recipes.objects.create(
            title="Sample Recipe",
            description="Sample description",
            image="media/post-5_A8VoxH3.jpeg/",
            is_active=True
        )
        recipe.products.add(product)

        response = self.client.get(f'/kk/recipes/{recipe.id}/')
        self.assertEqual(response.status_code, 200)