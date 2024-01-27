from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Product, RecipeIngredient


class CookbookTests(TestCase):
    def setUp(self):
        # Создаем объекты для тестирования
        self.recipe1 = Recipe.objects.create(name='Recipe 1')
        self.recipe2 = Recipe.objects.create(name='Recipe 2')
        self.product1 = Product.objects.create(name='Product 1')
        self.product2 = Product.objects.create(name='Product 2')

    def test_add_product_to_recipe(self):
        # Тестирование add_product_to_recipe
        url = reverse('cookbook:add_product_to_recipe', kwargs={'recipe_id': self.recipe1.id, 'product_id': self.product1.id, 'weight': 150})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')

    def test_cook_recipe(self):
        # Тестирование cook_recipe
        url = reverse('cookbook:cook_recipe', kwargs={'recipe_id': self.recipe1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')

    def test_show_recipes_without_product(self):
        # Тестирование show_recipes_without_product
        url = reverse('cookbook:show_recipes_without_product', kwargs={'product_id': self.product2.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_add_product_to_recipe_invalid_recipe(self):
        # Тестирование add_product_to_recipe с неверным идентификатором рецепта
        url = reverse('cookbook:add_product_to_recipe', kwargs={'recipe_id': 999, 'product_id': self.product1.id, 'weight': 150})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_add_product_to_recipe_invalid_product(self):
        # Тестирование add_product_to_recipe с неверным идентификатором продукта
        url = reverse('cookbook:add_product_to_recipe', kwargs={'recipe_id': self.recipe1.id, 'product_id': 999, 'weight': 150})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_cook_recipe_invalid_recipe(self):
        # Тестирование cook_recipe с неверным идентификатором рецепта
        url = reverse('cookbook:cook_recipe', kwargs={'recipe_id': 999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

