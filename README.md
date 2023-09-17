# Django

The project is written on the [Django](https://www.djangoproject.com) framework.
The backend is written in [python](https://www.python.org).
Frontend is written using [bootstrap](https://getbootstrap.com).
This is a website where anyone who wants to register can place an ad.

___

# Links and versions to the website    

* [Lebedev Sergey](https://github.com/LebedevSergeyV) – Product Lead & Fullstack Developer

* [Website](http://109.111.185.225) - a link to a website located on its server with a white (external) ip address connected. [LebedevSergeyV](https://github.com/LebedevSergeyV). A fresh and constantly updated version of the site.
  
* [Website](https://garage.xiver.ru) - link to the website on the server [GigantPro](https://github.com/GigantPro). Fucking great man. Previous version of the site. 


___

# Project deployment

#### The command to run the site docker build on the server [Debian](https://www.debian.org).
```commandline
sudo docker compose -f "./docker-compose.yml" up
```

#### The command to start the rebuild of the docker site on the server [Debian](https://www.debian.org).
```commandline
sudo docker compose -f "./docker-compose.yml" build --force-rm --no-cache
```

#### Clearing dockers data and file cache.
```commandline
docker image prune -a -f
```
___

# Django Commands

#### Running local the project locally.
```commandline
poetry run python manage.py runserver
```

##### Migrations in the Django project
```commandline
python manage.py makemigrations
```
```commandline
python manage.py migrate
```

___

# Documentation for each directory

* __[advertisements](advertisements%2Fadvertisements%2Fdoc.md)__
* __[app advertisements](advertisements%2Fapp_advertisements%2Fdoc.md)__
* __[app auth](advertisements%2Fapp_auth%2Fdoc.md)__
* __[templates](advertisements%2Ftemplates%2Fdoc.md)__
* __[static](advertisements%2Fstatic%2Fdoc.md)__
* __[media](advertisements%2Fmedia%2Fdoc.md)__
* __[commands](systemd%2Finfo.txt)__

___

[README.md](README.md)
