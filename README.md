# exchange_rate
# cookbook
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=5fe620)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=ffffff&color=5fe620)](https://www.djangoproject.com/)

### Краткое описание:
Django-приложение, которое отображает курс валюты по отношению к рублю на заданную дату. Данные по валютам хранятся в базе данных приложения. Для пополнения этой базы данных используется скрипт, который раз в сутки обращается к сервису ЦБ за актуальными курсами валют по адресу:
https://www.cbr-xml-daily.ru/daily_json.js

### Технологии проекта
* Python — высокоуровневый язык программирования.
* Django — высокоуровневый Python веб-фреймворк, который позволяет быстро создавать безопасные и поддерживаемые веб-сайты.

### Web-приложение предоставляет следующие HTTP функции, получающие параметры методом GET:
* rate/ с параметрами charcode и date. 
Например: http://127.0.0.1:8000/rate/?charcode=AUD&date=2024-01-01
Выводит результат в виде JSON в формате:
{
"charcode": "AUD",
"date": "2024-01-01",
"rate": 57.0627
}

### Шаблон наполнения .env

```bash
# секретный ключ Django
SECRET_KEY=
```

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone git@github.com:usdocs/exchange_rate.git
cd exchange_rate 
```

Cоздать и активировать виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
```

Обновить менеджер пакетов pip:
```bash
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:
```bash
pip3 install -r requirements.txt
```

Выполнить миграции:
```bash
python manage.py migrate
```

Создать суперпользователя:
```bash
python3 manage.py createsuperuser
```

Запустить проект:
```bash
python manage.py runserver
```


## Скрипт для сохранения актуальных курсов:
Команда для запуска скрипта для сохранения актуальных курсов:
```bash
python manage.py currency_data
```

Для ежедневного запуска скрипта необходимо:
1. Указать в файле getcurrencydata.sh актуальный путь к приложению.
2. Открыть конфигурационный файл с помощью команды:
```bash
crontab -e
```
3. Прописать команду:
```bash
@daily PATH_TO_APP/getcurrencydata.sh
```
PATH_TO_APP - путь к приложению, например: /home/ubuntu/exchange_rate


### Разработчик проекта

Автор: Andrey Balakin  
E-mail: [usdocs@ya.ru](mailto:usdocs@ya.ru)
