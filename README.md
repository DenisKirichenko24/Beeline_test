# Beeline_test

Установка зависимостей и запуск сервера

```sh
install requirements.txt
pip install -r requirements.txt
```

Так же будет необходимо локально развернуть каталог данных 

```sh
https://docs.open-metadata.org/deploy/local-deployment
```

После установки зависимостей и инициализации вы должны сделать миграции (не забудьте активировать виртуальное окружение)

```sh
python manage.py makemigrations
python manage.py migrate
```

Запуск сервера

```sh
python manage.py runserver
```