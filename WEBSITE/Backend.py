python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Импорт необходимых модулей
import cgi
import cgitb

# Включение отладочной информации
cgitb.enable()

# Заголовок страницы
print("Content-Type: text/html\n")

# HTML-код страницы
print("""
<!DOCTYPE html>
<html>
<head>
    <title>Мой сайт</title>
</head>
<body>
    <h1>Добро пожаловать на мой сайт!</h1>
    <p>Это главная страница.</p>
</body>
</html>
""")
