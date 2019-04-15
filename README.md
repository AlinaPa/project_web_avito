Типовой проект - клон сайта Avito
=======
Создан с целью обучения на курсах learn python

## Запуск проекта
1. Клонируем проект

        git clone https://github.com/AlinaPa/project_web_avito.git ~/projects/project_web_avito
    
2. Устанавливаем `pip` (менеджер python пакетов)

        pip3 install
     
3. Устанавливаем [python 3.6.5](https://www.python.org/downloads/release/python-365/)

4. Создаем виртуальное окружение

        python3 -m venv env

5. Активируем виртуальное окружение

        source env/bin/activate

6. Устанавливаем python пакеты

        pip install -r requirements/txt
        

## Настройка проекта
1. Создаем суперпользователя (так как база еще пуста)

        ./manage.py createsuperuser

2. Проводим миграции

        ./manage.py migrate

## Bulma
1. Установка

        npm install bulma

2. Документация [bulma v0.7.4](https://bulma.io/documentation/)
        