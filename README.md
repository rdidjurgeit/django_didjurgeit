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

## Running the test

Run the Python tests with the following command:

```
$ python manage.py test
```

## Deploying to production

The application will be deployed to Heroku, where the following needs to be configured:

- Create an app
- Set `SECRET_KEY` to a random value with 64 characters
- Set `DATABASE_URL` to the Code Institute PostgreSQL URL 
- Set `DISABLE_COLLECTSTATIC` to 1 to prevent collecstatic running each time
- Configure integration with GitHub and enable automatic deployments

Now each time a push to GitHub will trigger deployment. 

On Heroku use the option More > Run console to apply migrations with: 

```
$ python manage.py migrate
```

You can also create a super user:

```
$ python manage.py createsuperuser
```