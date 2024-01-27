from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.db.models import Sum
from .models import Product, Recipe, RecipeIngredient

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.db.models import Sum
from .models import Product, Recipe, RecipeIngredient


def add_product_to_recipe(request, recipe_id, product_id, weight):
    """
    Добавляет продукт к рецепту с указанным весом или изменяет вес, если продукт уже присутствует в рецепте.

    Parameters:
    - recipe_id (int): Идентификатор рецепта.
    - product_id (int): Идентификатор продукта.
    - weight (int): Вес продукта в граммах.

    Returns:
    - JsonResponse: JSON-ответ с результатом операции.
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)
    product = get_object_or_404(Product, id=product_id)

    recipe_ingredient, created = RecipeIngredient.objects.get_or_create(
        recipe=recipe, product=product, defaults={'weight': weight}
    )

    if not created:
        recipe_ingredient.weight = weight
        recipe_ingredient.save()

    return JsonResponse({'status': 'success'})


def cook_recipe(request, recipe_id):
    """
    Увеличивает количество приготовленных блюд для каждого продукта в указанном рецепте.

    Parameters:
    - recipe_id (int): Идентификатор рецепта.

    Returns:
    - JsonResponse: JSON-ответ с результатом операции.
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)

    for ingredient in recipe.recipeingredient_set.all():
        ingredient.product.times_cooked += 1
        ingredient.product.save()

    return JsonResponse({'status': 'success'})


def show_recipes_without_product(request, product_id):
    """
    Возвращает список рецептов, в которых указанный продукт отсутствует или присутствует в количестве менее 10 грамм.

    Parameters:
    - request (HttpRequest): Объект запроса.

    Returns:
    - HttpResponse: HTML-страница с результатами операции.
    """
    # product_id = request.GET.get('product_id', None)

    if product_id is not None:
        product = get_object_or_404(Product, id=product_id)
        recipes_without_product = Recipe.objects.exclude(
            recipeingredient__product=product,
            recipeingredient__weight__gte=10
        ).annotate(total_weight=Sum('recipeingredient__weight'))

        return render(request, 'cookbook/show_recipes_without_product.html', {'recipes_without_product': recipes_without_product})
    else:
        return HttpResponse("Пожалуйста, укажите в параметрах id продукта (product_id).")
