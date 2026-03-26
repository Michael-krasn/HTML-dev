## Требования

- Python 3.7 или выше
- pip (менеджер пакетов Python)

## Установка и запуск

### 1. Клонирование или распаковка проекта

Распакуйте архив с проектом в выбранную директорию.

### 2. Создание виртуального окружения (рекомендуется)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```
### Установка
pip install -r requirements.txt

### Запуск
python app.py

### Проверка
URL Описание
/ или /contacts Страница контактов (основная)
/home Главная страница с товарами
/catalog Каталог товаров с фильтрацией
/category/electronics Категория "Электроника"
/category/clothing Категория "Одежда"
/category/home Категория "Дом и сад"

