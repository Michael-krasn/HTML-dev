from flask import Flask, send_from_directory, render_template_string
import os

app = Flask(__name__, static_folder='.')


# Корневой путь - возвращает страницу контактов
@app.route('/')
def contacts():
    """Возвращает страницу контактов на любой GET-запрос"""
    try:
        with open('contacts.html', 'r', encoding='utf-8') as file:
            content = file.read()
        return content, 200, {'Content-Type': 'text/html; charset=utf-8'}
    except FileNotFoundError:
        return "<h1>404 - Страница не найдена</h1><p>Файл contacts.html отсутствует.</p>", 404


# Главная страница с товарами
@app.route('/home')
def home():
    """Возвращает главную страницу"""
    try:
        with open('index.html', 'r', encoding='utf-8') as file:
            content = file.read()
        return content, 200, {'Content-Type': 'text/html; charset=utf-8'}
    except FileNotFoundError:
        return "<h1>404 - Страница не найдена</h1><p>Файл index.html отсутствует.</p>", 404


# Страница каталога
@app.route('/catalog')
def catalog():
    """Возвращает страницу каталога"""
    try:
        with open('catalog.html', 'r', encoding='utf-8') as file:
            content = file.read()
        return content, 200, {'Content-Type': 'text/html; charset=utf-8'}
    except FileNotFoundError:
        return "<h1>404 - Страница не найдена</h1><p>Файл catalog.html отсутствует.</p>", 404


# Страница категории (с параметром)
@app.route('/category/<category_name>')
def category(category_name):
    """Возвращает страницу категории с динамическим содержимым"""
    try:
        with open('category.html', 'r', encoding='utf-8') as file:
            content = file.read()

        # Замена динамического контента в зависимости от категории
        category_titles = {
            'electronics': 'Электроника',
            'clothing': 'Одежда',
            'home': 'Дом и сад',
            'all': 'Все категории'
        }

        category_descriptions = {
            'electronics': 'Современные гаджеты и электронные устройства для всей семьи',
            'clothing': 'Стильная одежда для мужчин и женщин',
            'home': 'Товары для дома, сада и уюта',
            'all': 'Весь ассортимент нашего магазина'
        }

        title = category_titles.get(category_name, category_name.capitalize())
        description = category_descriptions.get(category_name, 'Товары в этой категории')

        # Простая замена в HTML (можно улучшить с использованием шаблонов)
        content = content.replace('Электроника', title)
        content = content.replace('Современные гаджеты и электронные устройства для всей семьи', description)

        return content, 200, {'Content-Type': 'text/html; charset=utf-8'}
    except FileNotFoundError:
        return "<h1>404 - Страница не найдена</h1><p>Файл category.html отсутствует.</p>", 404


# Общий обработчик для статических файлов
@app.route('/<path:filename>')
def static_files(filename):
    """Отдача статических файлов"""
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read(), 200, {'Content-Type': 'text/html; charset=utf-8'}
    return "<h1>404 - Файл не найден</h1>", 404


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
