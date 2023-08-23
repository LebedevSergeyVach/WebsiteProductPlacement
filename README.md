# Django

* [Lebedev_Sergey](https://github.com/LebedevSergeyV) – Product Lead & Developer

* [Website](http://109.111.185.225) - a link to a website located on its server with a white (external) ip address connected. [LebedevSergeyV](https://github.com/LebedevSergeyV). A fresh and constantly updated version of the site.
  
* [Website](https://garage.xiver.ru) - link to the website on the server [GigantPro](https://github.com/GigantPro). Fucking great man. Previous version of the site. 
* [Website](https://astonishing-pixie-c2446d.netlify.app/advertisements/templates/index.html) - Link to the website. Version without downloading the docker file on a free hosting [Netify](https://app.netlify.com).

The command to run the site docker build on the server [Debian](https://www.debian.org)
```commandline
su -c 'sudo docker compose -f "./docker-compose.yml" up'
```

The command to start the rebuild of the docker site on the server [Debian](https://www.debian.org)
```commandline
su -c 'sudo docker compose -f "./docker-compose.yml" build --force-rm --no-cache'
```

Running the project locally.
```commandline
poetry run python manage.py runserver
```
