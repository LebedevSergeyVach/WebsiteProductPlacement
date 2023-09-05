# Django

The project is written on the Django framework.
The backend is written in [python](https://www.python.org).
Frontend is written using [bootstrap](https://getbootstrap.com).
This is a website where anyone who wants to register can place an ad.

___

# Links and versions to the website    

* [Lebedev_Sergey](https://github.com/LebedevSergeyV) – Product Lead & Developer

* [Website](http://109.111.185.225) - a link to a website located on its server with a white (external) ip address connected. [LebedevSergeyV](https://github.com/LebedevSergeyV). A fresh and constantly updated version of the site.
  
* [Website](https://garage.xiver.ru) - link to the website on the server [GigantPro](https://github.com/GigantPro). Fucking great man. Previous version of the site. 


___

# Project deployment

The command to run the site docker build on the server [Debian](https://www.debian.org).
```commandline
su -c 'sudo docker compose -f "./docker-compose.yml" up'
```

The command to start the rebuild of the docker site on the server [Debian](https://www.debian.org).
```commandline
su -c 'sudo docker compose -f "./docker-compose.yml" build --force-rm --no-cache'
```

___

# Django Commands

Running the project locally.
```commandline
poetry run python manage.py runserver
```

Migrations in the Django project
```commandline
python manage.py migrate && python manage.py makemigrations
```

If poetry is present in the project
```commandline
poetry run python manage.py migrate && poetry run python manage.py makemigrations
```
