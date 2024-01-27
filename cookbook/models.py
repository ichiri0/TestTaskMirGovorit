from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255,
                            unique=True,
                            verbose_name="Наименование")
    times_cooked = models.IntegerField(default=0,
                                       verbose_name="Количество приготовлений")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Recipe(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name="Наименование")
    ingredients = models.ManyToManyField(Product,
                                         through='RecipeIngredient',
                                         verbose_name="Ингредиенты")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    weight = models.IntegerField()

    def __str__(self):
        return f"{self.product} ({self.weight} г.)"

    class Meta:
        verbose_name = 'Рецепт-Ингредиент'
        verbose_name_plural = 'Рецепт-Ингредиенты'
