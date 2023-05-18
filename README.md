# yamdb



Проект `Yamdb` с возможностью запуска через `Docker-compose`.



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



## Как развернуть проект на сервере:

### Склонировать репозиторий:

```python

git clone git@github.com:Pankirbor/yamdb_final.git

```
### Подготовка удаленного сервера для развертывания проекта:
- Выполнив вход на свой сервер, установите docker:

```python
sudo apt install docker.io
```
- Установите docker-compose:

```python
curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```
- Локально в проекте отредактируйте файл `infra/nginx/default.conf` изменив `IP-адрес` сервера.
- Скопируйте файлы `default.conf` и `docker-compose.yaml` насвой сервер, выполнив локально команды:

```python
# из дириктори infra
scp docker-compose.yml <username>@<host>:/home/<username>/docker-compose.yml

# из директории nginx
scp nginx.conf <username>@<host>:/home/<username>/nginx.conf
```
### `Workflow Action`:
- Создать необходимые секретные данные для доступа к `GitHub`, `DockerHub`, `своему серверу`, а так же наполнения `.env`:

```python
    DB_ENGINE=<django.db.backends.postgresql>
    DB_NAME=<имя базы данных postgres>
    POSTGRES_USER=<пользователь бд>
    POSTGRES_PASSWORD=<пароль>
    DB_HOST=<db>
    DB_PORT=<5432>

    DOC_PASSWORD=<пароль от DockerHub>
    DOCKER_USERNAME=<имя пользователя>

    SECRET_KEY=<секретный ключ проекта django>

    USER_SERVER=<username для подключения к серверу>
    SERVER_HOST=<IP сервера>
    PASSPHRASE=<пароль для сервера, если он установлен>
    SSH_KEY=<ваш SSH ключ (для получения команда: cat ~/.ssh/id_rsa)>

    TELEGRAM_TO=<ID чата, в который придет сообщение>
    TELEGRAM_TOKEN=<токен вашего бота>
```
### Процесс автоматизированой работы `Workflow Action`:
- После отправки изменеий на `github` (`git push origin master`) срабатывает триггер на запуск:
    - первым этапом, происходит тестирование проекта;
    - вторым этапом, происходит сборка образа и загрузка на `DockerHub`;
    - третий этап осуществляет разворачивание прокта на сервере на основе загруженного образа;
    - четвертый этап, отправка сообщения в чат телеграм об успешном результате.
    - **каждый этап выполняется только в случае успешного исполнения предыдущего.**

- Далее на сервере необходимо выполнить команды:

```python
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

    - [Адимн-зона сайта](http://yamdbkirill.sytes.net/admin/)

    - [Главная страница API](http://yamdbkirill.sytes.net/api/v1/)

    - [Документация к работе с API](http://yamdbkirill.sytes.net/redoc/)



## Создатель

- [Кирилл Панов](https://github.com/pankirbor)



[![master](https://github.com/pankirbor/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?branch=master)](https://github.com/Pankirbor/yamdb_final/actions)
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)