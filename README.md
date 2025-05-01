# NurdinovA_22apr2025

# My Test Project

## Описание

Этот проект предназначен для тестирования функциональности корзины интернет-магазина на сайте `https://altaivita.ru`. Он включает в себя набор UI и API автотестов, написанных с использованием Pytest, Selenium и Allure для отчетности. Проект позволяет тестировать основные операции с корзиной: добавление товаров, изменение количества, получение содержимого и удаление товаров.

## Структура проекта
- `config.py`: содержит конфигурационные данные для API-запросов.
- `api/`: модуль для работы с API сайта.
  - `cart_api.py`: классы и методы для взаимодействия с API корзины.
- `pages/`: модуль для работы с UI-страницами.
  - `base_page.py`: базовые методы для работы с элементами страниц.
  - `main_page.py`: класс и методы для взаимодействия с главной страницей.
  - `cart_page.py`: класс и методы для взаимодействия со страницей корзины.
- `tests/`: модуль с тестами.
  - `test_cart.py`: тесты для проверки операций в UI корзине.
  - `test_api.py`: тесты для проверки операций в API корзине.
- `requirements.txt`: список зависимостей проекта.
- `pytest.ini`: конфигурация для Pytest.

## Установка и настройка

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/yourusername/my_test_project.git
   cd my_test_project
   ```
   
2. **Создайте и активируйте виртуальное окружение:**
   
   ```bash
    python -m venv venv
    source venv/bin/activate   # Для Linux/MacOS
    venv\Scripts\activate      # Для Windows
   ```
   
3. **Установите зависимости:**
  
    ```bash
    pip install -r requirements.txt
    ```
   
4. **Установите Allure:**
    ```bash
    Установите Allure с https://allurereport.org/docs/install-for-windows/
   ```

5. **Проверьте установку Allure:**
    ```bash
    allure --version
    ```

## Запуск тестов

1. **Запуск всех тестов:**

    ```bash
    pytest --alluredir=allure-results
    ```
Или

```bash
    python -m pytest --alluredir allure-results
```

2. **Запуск тестов с отчетом Allure:**
После выполнения тестов, отчет Allure можно сгенерировать и просмотреть следующим образом:
    ```bash
    allure serve allure-results
    ```
   
## Структура тестов

### Обзор

- `test_cart.py` содержит UI тесты, которые используют Selenium для проверки взаимодействий с веб-интерфейсом.
- `test_api.py` содержит API тесты, которые используют requests для проверки API функциональности корзины.

### Основные тесты

- `UI тесты`:
  - `test_add_product_to_cart`
  - `test_increase_product_quantity`
- `API тесты`:
  - `test_add_product_to_cart`
  - `test_update_product_quantity`
  - `test_get_cart_contents`
  - `test_remove_product_from_cart`