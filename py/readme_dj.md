##Установка окружения

-создание окружения
    python -m venv .Folder_name
-Активация окружения (deactivate - деактивировать)
    ..\Scripts\activate.bat

##джанго
-pip django
-pip freeze (отслеживание, что установлены все зависимости)
-django-admin -h (список команд)

##создание  и работа с проектом
-first_project - наименование
-django-admin - команда
-startproject - ключ команды

-----------------
python manage.py runserver (запуск тестового сервера (в папке проекта созданного джанго))
-----------------

 django-admin startproject first_project (после запуска создается папка с наименованием проекта)

 python manage.py startapp first_app (создание нового приложения с именем)
  
 python manage.py createsuperuser


**миграции
 python manage.py migrate (джанго выполняет требуемые миграции)
 python manage.py makemigrations (создание миграций для моделей и приложений)


python manage.py shell


//15-10-20
10 (привязка интренет адресов)