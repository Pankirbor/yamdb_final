# yamdb



Проект `Yamdb` с возможностью запуска через контейнер в `Docker`.



## Технологии:

- `YaMDb` - приложение, собирает отзывы пользователей на произведения. Произведения делятся на категории,

 такие как «Книги», «Фильмы», «Музыка», которым может быть присвоен жанр. Благодарные или возмущённые пользователи

оставляют к произведениям текстовые отзывы и ставят свои оценки, на основе которых формируется рейтинг.

Так же можно оставлять отзывы и комментарии.

- `REST API для Yatube` - это интерфейс через, который смогут работать мобильные приложения или чат-бот.

 Либо передавать данные в веб-приложение или на фронтенд.

- `Docker-compose` - для развертки приложения в контейнерах с использованием всех необходимых зависимостей Ganicrion и NGINX.

- `PostgreSQL` - база данных для хранения всех записей.



## Что нужно для старта

- `python3.7`

- `Docker version 23.0.4`

- `docker-compose version 1.25.0`

- `.env.example`


```python

# ...директория_проекта yamdb_final/infra/.env

# Укажите, что используете postgresql

DB_ENGINE=django.db.backends.postgresql

# Укажите имя созданной базы данных

DB_NAME=name_db

# Укажите имя пользователя

POSTGRES_USER=user

# Укажите пароль для пользователя

POSTGRES_PASSWORD=password

# Укажите localhost

DB_HOST=db

# Укажите порт для подключения к базе

DB_PORT=5432

# секретный ключ из папки settings.py

SECRET_KEY = 'SECRET_KEY_из_настроек_проекта'

```



## Как развернуть проект с помощью `docker-compose` на локальном сервере:

- перейдите в директорию `./infra` и выполните следующие команды в терминале:



```python

# запуск сборки образов и контейнеров

sudo docker-compose up



# запуск миграций

sudo docker-compose exec web python manage.py migrate



# создание суперюзера для входа в админ-зону

sudo docker-compose exec web python manage.py createsuperuser



# сбор всей статики для корректного отображения страниц

sudo docker-compose exec web python manage.py collectstatic --no-input



# вход в оболочку для очистки контент данных

sudo docker-compose exec web python manage.py shrell



>>> from django.contrib.contenttypes.models import ContentType

>>> ContentType.objects.all().delete.()

>>> quit()



# загрузка фиктур для базы данных

sudo docker-compose exec web python manage.py loaddata fixtures.json



```

- ссылки на работающий проект:

    - http://yamdbkirill.sytes.net/admin/

    - http://yamdbkirill.sytes.net/api/v1/

    - http://yamdbkirill.sytes.net/redoc/



## Создатель

- [Кирилл Панов](https://github.com/pankirbor)



![master](https://github.com/pankirbor/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?branch=master)
