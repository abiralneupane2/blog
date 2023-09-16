# blog
## This project was created as specification provided by ramailo tech
### Feel free to use it as you please.

## python=>3.10

### make sure redis is running in port 6379

> docker run --name some-redis -d redis

> pip install -r requirements.txt

### cd into blog/mysite

> python manage.py migrate
> python manage.py createsuperuser --noinput --username admin --password admin

> python manage.py runserver

### api docs available at /docs

