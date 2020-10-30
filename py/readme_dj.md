##курс
https://www.youtube.com/watch?v=zdonFVX6fQc&list=PLD-piGJ3Dtl0v10rx98Q0kuAsBfn2MmxL&index=6
https://django.fun/videos/uroki-django-sozdanie-sajta-urok-1-chto-takoe-django/

20-10-20
https://django.fun/tutorials/flask-vs-django-sravnenie-sozdaniya-rest-api/
21-10-20
https://www.youtube.com/watch?v=dKdkuYXylx8
https://www.youtube.com/watch?v=lsAbq2RcWlQ&feature=emb_logo (создание погодного приложения)

##Текст рыба
https://gsgen.ru/tools/fish-text/

##Установка окружения
-создание окружения
    python -m venv .venv
-Активация окружения (deactivate - деактивировать)
    ..\Scripts\activate.bat

##джанго
-----------------
python manage.py runserver (запуск тестового сервера (в папке проекта созданного джанго))
-----------------

- pip install django (по умолчанию устанавливается последняя, другая: pip install -U django==2.1.5)
- pip freeze (отслеживание, что установлены все зависимости)
- django-admin -h (список команд)


 django-admin startproject weather_prj (после запуска создается папка с наименованием проекта)

 python manage.py startapp first_app (создание нового приложения с именем) 


**миграции
 python manage.py makemigrations (создание миграций для моделей и приложений)
 python manage.py migrate (джанго выполняет требуемые миграции)

##БД
python manage.py createsuperuser (после первой миграции)


python manage.py shell

##Шаблоны джанго
Директивы, теги, Фильтры


----------------------------------------------------------------------------
https://www.django-rest-framework.org/
----------------------------------------------------------------------------
//инструмент тестирования 
https://www.postman.com/products/

pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
