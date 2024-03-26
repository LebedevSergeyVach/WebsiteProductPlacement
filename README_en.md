# Website Product Placement 
# Production and software for Windows

The project is written on the [Django](https://www.djangoproject.com) framework.
The backend is written in [python](https://www.python.org).
Frontend is written using [bootstrap](https://getbootstrap.com).
This is a website where anyone who wants to register can place an ad.

___

# Links and versions to the website    

* [Lebedev Sergey Vyacheslav](https://github.com/LebedevSergeyVach) – Product Lead & Fullstack Developer.

* [Website](https://serphantom.space) - a link to a website located on its server with a white (external) ip address connected. [LebedevSergeyVach](https://github.com/LebedevSergeyVach). A fresh and constantly updated version of the site.

___

# Project deployment on the server [Debian](https://www.debian.org).

#### Download a project.
```commandline
git clone git@github.com:LebedevSergeyVach/WebsiteProductPlacement.git
```
#### The command for configuring and migrating the project database on the Django framework on the server.
```commandline
python manage.py makemigrations
```
```commandline
python manage.py migrate
```
#### Creating and configuring a website administrator.
```commandline
python manage.py createsuperuser
```
#### The command to start the rebuild of the docker site on the server [Debian](https://www.debian.org).
```commandline
sudo docker compose -f "./docker-compose.yml" build --force-rm --no-cache
```
#### The command to run the site docker build on the server [Debian](https://www.debian.org).
```commandline
sudo docker compose -f "./docker-compose.yml" up
```
#### Clearing dockers data and file cache.
```commandline
sudo docker builder prune
```
___

## Documentation for each directory

* `The main application of the framework` - [advertisements](advertisements%2Fadvertisements%2FREADME.md)
* `The main application of the project` - [app advertisements](advertisements%2Fapp_advertisements%2FREADME.md)
* `Authorization application` - [app auth](advertisements%2Fapp_auth%2FREADME.md)
* `Project Template Directory` - [templates](advertisements%2Ftemplates%2FREADME.md)
* `Directory of static project files` - [static](advertisements%2Fstatic%2FREADME.md)
* `The directory of the project's media files` - [media](advertisements%2Fmedia%2FREADME.md)


## List of the main commands used in the project

* `Project Console commands` - [commands](advertisements%2FREADME.md)

___

`README` - [README.md](README.md)
