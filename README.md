# To do app

This is a todo app

## Running the project

Start the server with the following command:

```
$ python manage.py runserver 
```

## Generating and applying migrations 

Modify models in the models.py file and then run the following command:

```
$ python manage.py makemigrations todo
```

Note that this will just generate the migration but it still needs to be applied with the following command:

```
$ python manage.py migrate blog
```

## Accessing the admin interface

The admin interface is accessible at `/admin`. To log in, first create a superuser with the following command:

```
$ python manage.py createsuperuser
```