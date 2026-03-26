from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='.')

# Корневой путь - возвращает страницу контактов
@app.route('/')
@app.route('/contacts')
def contacts():
    """Возвращает страницу контактов на любой GET-запрос"""
    try:
        with open('contacts.html', 'r', encoding='utf-8') as file:
            content = file.read()
        return content, 200, {'Content-Type': 'text/html; charset=utf-8'}
    except FileNotFoundError:
        return "<h1>404 - Страница не найдена</h1><p>Файл contacts.html отсутствует.</p>", 404

# Дополнительный маршрут для главной страницы (опционально)
@app.route('/home')
def home():
    """Возвращает главную страницу"""
    try:
        with open('index.html', 'r', encoding='utf-8') as file:
            content = file.read()
        return content, 200, {'Content-Type': 'text/html; charset=utf-8'}
    except FileNotFoundError:
        return "<h1>404 - Страница не найдена</h1><p>Файл index.html отсутствует.</p>", 404

# Для статических файлов (если понадобятся)
@app.route('/<path:filename>')
def static_files(filename):
    """Отдача статических файлов"""
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read(), 200, {'Content-Type': 'text/html; charset=utf-8'}
    return "<h1>404 - Файл не найден</h1>", 404

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
