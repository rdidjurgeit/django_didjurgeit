# To-Do App

This is a to-do app built with Django, allowing users to manage their tasks effectively.

## Table of Contents

1. <details open>
    <summary><a href="#overview">Overview</a></summary>
</details>

2. <details open>
    <summary><a href="#getting-started">Getting Started</a></summary>
    <ul>
        <li><details>
            <summary><a href="#running-the-project">Running the Project</a></summary>
        </details></li>
        <li><details>
            <summary><a href="#generating-and-applying-migrations">Generating and Applying Migrations</a></summary>
        </details></li>
    </ul>
</details>

3. <details open>
    <summary><a href="#admin-interface">Admin Interface</a></summary>
</details>

4. <details open>
    <summary><a href="#testing">Testing</a></summary>
</details>

5. <details open>
    <summary><a href="#deployment">Deployment</a></summary>
</details>

6. <details open>
    <summary><a href="#features">Features</a></summary>
</details>

7. <details open>
    <summary><a href="#technologies-used">Technologies Used</a></summary>
</details>

8. <details open>
    <summary><a href="#credit-and-contact">Credit and Contact</a></summary>
</details>

---

## Overview

This application allows users to create, edit, and delete tasks, with the added feature of user authentication to ensure that each user can only see their own tasks.

## Getting Started

### Running the Project

If this project is cloned from the repository, first install the required packages using the following command:

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

## Credits and Contact

The base.html 

was take as exemple the one provide in during the Blog run creation and adapt.

