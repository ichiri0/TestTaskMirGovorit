
# Приложение Cookbook

Приложение Cookbook - это веб-приложение на Django для управления рецептами и ингредиентами.

## Установка

1. Клонировать репозиторий:

   ```bash
   git clone https://github.com/ichiri0/TestTaskMirGovorit.git
   ```

2. Перейти в директорию проекта:

   ```bash
   cd ваше-приложение-cookbook
   ```

3. Создать виртуальное окружение (по желанию, но рекомендуется):

   ```bash
   python -m venv venv
   ```

4. Активировать виртуальное окружение:

   - На Windows:

     ```bash
     venv\Scripts\activate
     ```

   - На macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. Установить зависимости:

   ```bash
   pip install -r requirements.txt
   ```

6. Применить миграции базы данных:

   ```bash
   python manage.py migrate
   ```

## Использование

1. Запустить сервер разработки:

   ```bash
   python manage.py runserver
   ```

2. Открыть веб-браузер и перейти по адресу [http://localhost:8000/cookbook/](http://localhost:8000/cookbook/) для доступа к приложению Cookbook.

## Конечные точки

- **Добавить продукт к рецепту:**

  ```http
  GET /cookbook/add_product_to_recipe/<int:recipe_id>/<int:product_id>/<int:weight>/
  ```

- **Приготовить рецепт:**

  ```http
  GET /cookbook/cook_recipe/<int:recipe_id>/
  ```

- **Показать рецепты без продукта:**

  ```http
  GET /cookbook/show_recipes_without_product/<int:product_id>/
  ```

## Тестирование

Чтобы запустить тесты, воспользуйтесь следующей командой:

```bash
python manage.py test
```


## Лицензия

Этот проект лицензирован под MIT License - см. файл [LICENSE](LICENSE) для подробностей.

