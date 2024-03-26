# Размещение продукции на веб-сайте
# Продукция и программное обеспечение для Windows

Проект написан на фреймворке [Django](https://www.djangoproject.com).
Бэкенд написан на [Python](https://www.python.org).  
Фронтенд разработан с использованием [Bootstrap](https://getbootstrap.com).  
Это веб-сайт, на котором любой желающий, после прохождения регистрации, может разместить объявление о продаже товара или услуги.

---

## Ссылки и версии веб-сайта    
* [Лебедев Сергей Вячеславович](https://github.com/LebedevSergeyVach) – Ведущий разработчик и Fullstack-разработчик.
* [Веб-сайт](https://serphantom.space) - ссылка на веб-сайт, размещенный на собственном сервере с белым (внешним) IP-адресом. [LebedevSergeyVach](https://github.com/LebedevSergeyVach). Свежая и постоянно обновляемая версия сайта.

---

## Развертывание проекта на сервере [Debian](https://www.debian.org).

#### Загрузка проекта.
```commandline
git clone git@github.com:LebedevSergeyVach/WebsiteProductPlacement.git
```
#### Команда для настройки и миграции базы данных проекта на фреймворке Django на сервере.
```commandline
python manage.py makemigrations
```
```commandline
python manage.py migrate
```
#### Создание и настройка администратора веб-сайта.
```commandline
python manage.py createsuperuser
```
#### Команда для запуска сборки сайта в docker на сервере.
```commandline
sudo docker compose -f "./docker-compose.yml" build --force-rm --no-cache
```
#### Команда для запуска docker-сборки сайта на сервере.
```commandline
sudo docker compose -f "./docker-compose.yml" up
```
#### Очистка данных docker и файлового кэша.
```commandline
sudo docker builder prune
```

---

## Документация для каждого каталога
* `Главное приложение фреймворка` - [advertisements](advertisements%2Fadvertisements%2FREADME.md)
* `Основное приложение проекта` - [app advertisements](advertisements%2Fapp_advertisements%2FREADME.md)
* `Приложение авторизации проекта` - [app auth](advertisements%2Fapp_auth%2FREADME.md)
* `Директория шаблонов проекта` - [templates](advertisements%2Ftemplates%2FREADME.md)
* `Директория статических файлов проекта` - [static](advertisements%2Fstatic%2FREADME.md)
* `Директория медиа файлов проекта` - [media](advertisements%2Fmedia%2FREADME.md)

## Список основных команд, используемых в проекте
* `Консольные команды проекта` - [commands](advertisements%2FREADME.md)

___

`README` - [README.md](README.md)