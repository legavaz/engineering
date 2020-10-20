##курс
https://www.youtube.com/watch?v=zdonFVX6fQc&list=PLD-piGJ3Dtl0v10rx98Q0kuAsBfn2MmxL&index=6

##Текст рыба
https://gsgen.ru/tools/fish-text/

##Установка окружения

-создание окружения
    python -m venv .Folder_name
-Активация окружения (deactivate - деактивировать)
    ..\Scripts\activate.bat

##джанго
- pip install django
- pip freeze (отслеживание, что установлены все зависимости)
- django-admin -h (список команд)


 django-admin startproject first_project (после запуска создается папка с наименованием проекта)

 python manage.py startapp first_app (создание нового приложения с именем)
  
 python manage.py createsuperuser

-----------------
python manage.py runserver (запуск тестового сервера (в папке проекта созданного джанго))
-----------------


**миграции
 python manage.py migrate (джанго выполняет требуемые миграции)
 python manage.py makemigrations (создание миграций для моделей и приложений)


python manage.py shell

##Шаблоны джанго
Директивы, теги, Фильтры