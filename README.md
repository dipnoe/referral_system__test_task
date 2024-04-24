Проект является тестовым заданием.

**Технологический стек:** Python | Django | DRF | PostgreSQL | Docker

# referral_system

# Запуск проекта

1. Склонируйте git-репозиторий
    ```bash
       git clone git@github.com:dipnoe/referral_system__test_task.git
    ```

2. Зайдите в корень проекта командой `cd <путь-до-дирректории-проекта>`


3. Создайте `.env` из файла `.env.dist` командой `cp .env.dist .env`. 
Для генерации ключа Django вызовите команду 
    ```bash
    echo "SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')" >> .env
    ```


4. Запустите приложение с помощью `docker-compose` (используется утилита `make`)
    ```bash
    make docker-up
    ```

- Для работы приложения подготовлена коллекция postman.
  Необходимо импортировать файл `postman/Referral_system.postman_collection.json` в свой postman
  ([Как импортировать коллекцию в postman](https://docs.rkeeper.ru/api/testirovanie-zaprosov-v-postman-87557103.html#id-%D0%A2%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D0%BE%D0%B2%D0%B2Postman-%D0%98%D0%BC%D0%BF%D0%BE%D1%80%D1%82%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D0%B9)).
  Коллекция не требует дополнительной конфигурации, в запросах используется автоматическая
  подстановка случайных мок-значений для удобства.

- Затем последовательно выполните запросы из папки `user 1`, чтобы создать первого пользователя 
и иметь возможность использовать его инвайт код:
    - `Auth` для получения кода аутентификации;
    - `Verify` прохождение верификации, получение инвайт-кода и токена;
    - `Get user` получение профиля пользователя;
- После этого перейдите в папку `user 2` и повторите действия, добавив запрос:
  - `Add invited code to user 2` на добавление инвайт кода;

Затем нужно снова выполнить запрос `Get user` из папки `user 1`, чтобы убедиться, что в API профиля выводится
список пользователей(номеров телефона), которые ввели инвайт код текущего пользователя.


### Команды для работы в Docker

Для сборки и запуска проекта в Docker используйте команду:

```bash
make docker-up
```

Для остановки Docker-контейнеров:

```bash
make docker-down
```

Для ручного входа в контейнер django-приложения:

```bash
make docker-exec
```

### Документация приложения будет доступна по адресу:

- http://localhost:8000/redoc/