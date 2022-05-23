работа №24
API by Flask

Описание проекта
Установка зависимостей
pip install -r requirements.txt

Создание/пересоздание базы данных: 
create_bd.py

Запуск проекта:
Bash (Linux/MACOS)
export FLASK_APP=run.py
export FLASK_ENV='development'
flask run

CMD (Windows)
set FLASK_APP=run.py
set FLASK_ENV=development
flask run

Для регистрации пользователя отправляется запрос вида
{"email": "mich1@mail.ru", "password": "mi-mi-mi", "name": "mich1"}
по маршруту
http://localhost:5000/auth/register