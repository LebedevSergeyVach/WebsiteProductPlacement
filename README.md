# Website Product Placement 
# Production and software for Windows

The project is written on the [Django](https://www.djangoproject.com) framework.
The backend is written in [python](https://www.python.org).
Frontend is written using [bootstrap](https://getbootstrap.com).
This is a website where anyone who wants to register can place an ad.

___

# Links and versions to the website    

* [Lebedev SergeyVach](https://github.com/LebedevSergeyVach) – Product Lead & Fullstack Developer

* [Website](http://109.111.185.225) - a link to a website located on its server with a white (external) ip address connected. [LebedevSergeyVach](https://github.com/LebedevSergeyVach). A fresh and constantly updated version of the site.

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
sudo docker builder prune
```
___

## Documentation for each directory

* [advertisements](advertisements%2Fadvertisements%2FREADME.md)
* [app advertisements](advertisements%2Fapp_advertisements%2FREADME.md)
* [app auth](advertisements%2Fapp_auth%2FREADME.md)
* [templates](advertisements%2Ftemplates%2FREADME.md)
* [static](advertisements%2Fstatic%2FREADME.md)
* [media](advertisements%2Fmedia%2FREADME.md)

## List of the main commands used in the project

* [commands](advertisements%2FREADME.md)

___

[README.md](README.md)
