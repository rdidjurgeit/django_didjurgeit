# To do app

This is a todo app

## Running the project

In case this project is been clone from the repository. First you need to install the requirements.txt, using the following command:

```
$ pip install -r requirements.txt
```

Run the migration with the following command:

```
$ python manage.py migrate
```

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
$ python manage.py migrate todo
```

## Accessing the admin interface

The admin interface is accessible at `/admin`. To log in, first create a superuser with the following command:

```
$ python manage.py createsuperuser
```