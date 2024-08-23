
# Mountain Passes API

Проект Mountain Passes предоставляет API для работы с информацией о горных перевалах. Это API включает возможности добавления, редактирования, удаления и просмотра информации о различных перевалах.

## Установка и настройка

### Требования

- Python 3.11
- Django 5.0.7
- PostgreSQL

### Установка

1. **Клонируйте репозиторий:**

    ```bash
    git clone <URL вашего репозитория>
    cd mountain_passes
    ```

2. **Создайте виртуальное окружение:**

    ```cmd
    python -m venv .venv
    ```

3. **Активируйте виртуальное окружение:**

    ```cmd
    .venv\Scripts\activate
    ```

4. **Установите зависимости:**

    ```cmd
    pip install -r requirements.txt
    ```

5. **Настройте базу данных:**

    Создайте базу данных PostgreSQL и примените миграции:

    ```cmd
    python manage.py migrate
    ```

6. **Создайте суперпользователя:**

    ```cmd
    python manage.py createsuperuser
    ```

7. **Запустите сервер разработки:**

    ```cmd
    python manage.py runserver
    ```

## Использование API

После запуска сервера API будет доступно по адресу `http://localhost:8000/`.

### Основные эндпоинты:

- `GET /passes/` — Получить список всех перевалов.
- `POST /passes/` — Добавить новый перевал.
- `GET /passes/<id>/` — Получить информацию о конкретном перевале.
- `PATCH /passes/<id>/` — Обновить информацию о перевале.
- `DELETE /passes/<id>/` — Удалить перевал.

## Тестирование

Для запуска тестов используйте команду:

```cmd
python manage.py test
```

## Документация API с помощью Swagger

Для того чтобы упростить разработку и тестирование API, в проект интегрирован Swagger с использованием библиотеки `drf-yasg`. Swagger предоставляет интерактивную документацию, которая позволяет разработчикам легко просматривать и тестировать доступные API-эндпоинты.

### Настройка Swagger

Для использования Swagger необходимо убедиться, что приложение `drf_yasg` добавлено в `INSTALLED_APPS` вашего проекта Django:

```python
INSTALLED_APPS = [
    ...,
    'drf_yasg',
]
```

Также необходимо настроить URL для Swagger в вашем `urls.py`:

```python
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Mountain Passes API",
      default_version='v1',
      description="Документация для API проекта Mountain Passes",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ...,
]
```

### Доступ к документации

После настройки вы можете получить доступ к Swagger UI по следующему URL:

- **Swagger UI**: `http://localhost:8000/swagger/` — Интерактивная документация API, где можно просматривать и тестировать эндпоинты.

### Примеры использования API

Swagger UI позволяет не только просматривать документацию, но и отправлять реальные запросы к вашему API. Это полезно для тестирования и проверки правильности работы эндпоинтов.

1. Перейдите по адресу `http://localhost:8000/swagger/`.
2. Выберите интересующий вас эндпоинт из списка.
3. Нажмите на него, чтобы раскрыть детали запроса.
4. Заполните необходимые параметры (если есть).
5. Нажмите кнопку "Execute" для отправки запроса.
