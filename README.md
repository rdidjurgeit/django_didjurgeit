# Project 4 To-Do App

To-Do App is a Django-based task management application designed to help users efficiently manage their daily tasks. With a focus on simplicity and usability, the app allows users to create, edit, delete, and track tasks effortlessly.

## Table of Contents

- [Project 4 To-Do App](#project-4-to-do-app)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
    - [Technologie Used](#technologie-used)
  - [UX](#ux)
    - [Key UX Features](#key-ux-features)
    - [User Flow](#user-flow)
  - [Getting Started](#getting-started)
    - [Deploying to production](#deploying-to-production)
    - [Running the Project Locally](#running-the-project-locally)
    - [Generating and applying migrations](#generating-and-applying-migrations)
    - [Accessing the admin interface](#accessing-the-admin-interface)
  - [Test](#test)
    - [Frontend Testing](#frontend-testing)
      - [HTML Validation](#html-validation)
      - [CSS Validation](#css-validation)
      - [Manual UI Testing](#manual-ui-testing)
      - [JavaScript Testing](#javascript-testing)
    - [Backend Testing](#backend-testing)
      - [Authentication \& Authorization](#authentication--authorization)
      - [Task Management](#task-management)
      - [Pep8](#pep8)
      - [Automated Testing](#automated-testing)
  - [Credits and Contact](#credits-and-contact)

---

## Overview

- User Authentication: Secure user registration, login, and logout functionality.
- Personalized Task Management: Users can manage their tasks in a private workspace.
- Task Status Tracking: Tasks can be marked as Not Started, In Progress, or Completed.
- Premium Membership Support: Premium users gain access to enhanced features such as setting due dates for tasks.
- Responsive UI: Built with Bootstrap 5 for an elegant and mobile-friendly design.
- Search Functionality: Easily find tasks using keyword search.
- Membership Management: Activate or cancel premium membership directly from the app.

### Technologie Used

 __Backend:__ Django 4.2.16

 __Frontend:__ Bootstrap 5, Crispy Forms

 __Database:__ SQLite

 __HTML5:__ Use for html interface.

 __CSS3:__ For style the UX from the website.

---

## UX

The To-Do App prioritizes an intuitive and seamless User Experience (UX) to ensure users can efficiently manage their tasks with minimal effort. The app focuses on clarity, ease of navigation, and user-centric design to create a satisfying experience across devices. The idea is less is more. not much color where use keeping the basic know association like for example "cancel" usually is read.

- Effortless Task Management: Users can easily create, edit, delete, and track tasks.
- Personalized Workspace: Users only see and manage their tasks after logging in.
- Efficient Navigation: Clear and logical navigation makes finding features simple.
- Productivity-Enhancing Features: Premium users can set task due dates for better task organization.

### Key UX Features

__User Authentication:__

- Easy sign-up and login process.
- Clear validation messages for incorrect credentials.

__Task Dashboard:__

- All tasks displayed in a structured list.
- Ability to filter tasks by status or search keywords.
  
__Task Actions:__

- Edit or delete tasks with a single click.
- Toggle task status (Not Started → In Progress → Completed).

__Premium Membership:__

- Clear visual indicators for membership status.
- Easy activation or cancellation of premium membership.

__Error Handling:__

- Friendly error messages for restricted actions (e.g., editing another user’s task).
- Redirection to login for unauthorized users.

### User Flow

- Registration/Login: New users sign up or existing users log in.
- Dashboard Access: Access task lists, search, and filters.
- Task Management: Create, edit, delete, and toggle tasks.
- Membership Management: Activate or cancel premium features.
- Logout: Securely exit the application.

---

## Getting Started

There is many option to Star the project use an IDE of your choice, such as [Visual Studio Code](https://code.visualstudio.com/).

Ensure you have the following installed on your system:

- Python 3.8: [Download Python 3.8+](https://www.python.org/downloads/)
- pip – Python package manager (comes with Python installation)
- [Git](https://git-scm.com/)
  - You will have to set up a connection with an email
- Virtual Environment (optional but recommended)

### Deploying to production

The application will be deployed to Heroku, where the following needs to be configured:

- Create an app
- Set `SECRET_KEY` to a random value with 64 characters
- Set `DATABASE_URL` to the Code Institute PostgreSQL URL
- Set `DISABLE_COLLECTSTATIC` to 1 to prevent collecstatic running each time
- Configure integration with GitHub and enable automatic deployments

Now each time a push to GitHub will trigger deployment.

On Heroku use the option More > Run console to apply migrations with:

```
python manage.py migrate
```

You can also create a super user:

```
python manage.py createsuperuser
```

### Running the Project Locally

- For Local Deployment you will need to go to the GitHub  [Repository](https://github.com/rdidjurgeit/django_didjurgeit), find the Local tap, and close using the web URL. our Downloading as a Zip file.

If this project is cloned from the repository, first install the required packages using the following command:

```
pip install -r requirements.txt
```

Run the migration with the following command:

```
python manage.py migrate
```

Start the server with the following command:

```
python manage.py runserver 
```

### Generating and applying migrations

If you decide to change something  in the  models.py some times you will have to run the following command so the change can be valid:

```
python manage.py makemigrations
```

Note that this will just generate the migration but it still needs to be applied with the following command:

```
python manage.py migrate
```

### Accessing the admin interface

The admin interface is accessible at `/admin`. To log in, first create a superuser with the following command:

```
python manage.py createsuperuser
```

## Test

The application was tested on the following browsers:

- Firefox: Version 70.0.1
- Opera: Version 63.0.3
- Google Chrome: Version 77.0.3
- Microsoft Edge: Version 88.0.705
- Safari: Version 14.0
- Responsiveness Testing:

Conducted using Chrome Developer Tools across different device resolutions (Mobile, Tablet, Desktop).

### Frontend Testing

#### HTML Validation

- Tool Used: [W3C Markup Validation Service](https://validator.w3.org/)

- The HTML code was validated to ensure proper structure and adherence to standards.

![Validation](/img/w3validator.png)

---

#### CSS Validation

- Tool Used: [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

- CSS styles were validated to ensure responsiveness and cross-browser compatibility.

![ValidationCss](/img/w3css.png)

---

#### Manual UI Testing

1. Navigation Tests:

    - Click on the logo to verify redirection to the Home page.
    - Click on Home, Login, and Register links and verify navigation.
  
2. Authentication Pages:

    - Click on Login and ensure redirection to the login.html page.
    - Click on Register and verify redirection to the register.html page.
  
3. Task Management:

    - Click on New Task and verify access to the task_create.html page.
    - Edit an existing task and verify updates are reflected.
    - Delete a task and verify it is removed from the task list.

4. Membership Page:

    - Click on Membership and verify access to membership.html.
    - Test activation and cancellation of premium membership.

5. Search Functionality:

    - Enter a keyword in the Search bar and verify the correct tasks are displayed.

6. ask Status Toggle:

    - Verify tasks toggle correctly between Not Started → In Progress → Completed.

---

#### JavaScript Testing

- Form Validation
  - Attempt to submit a new task form with a blank title. Verify an error message appears.
  - Attempt to register with mismatched passwords. Verify an error message appears.

- Interactive Elements
  - Verify task status toggle buttons update status in real-time.
  - Ensure confirmation dialogs appear when deleting tasks.
  - Verify that task search updates results dynamically without page reload.

---

### Backend Testing

#### Authentication & Authorization

- Log in with an incorrect username and verify an error message appears.
- Log in with a correct username and password and verify redirection to the Task List page.
- Attempt to edit/delete another user's task and ensure an error message appears.
- Log out and verify redirection to the Login page.
- Test password reset functionality:
- Request a password reset.
- Verify receipt of an email.
- Complete password reset and log in with the new password.

#### Task Management

- Log in with an incorrect username and verify an error message appears.
- Log in with a correct username and password and verify redirection to the Task List page.
- Attempt to edit/delete another user's task and ensure an error message appears.
- Log out and verify redirection to the Login page.

#### Pep8

PEP8 is the official style guide for Python code, providing conventions for writing clean, readable, and consistent Python code. It ensures better collaboration, easier maintenance, and reduces bugs by standardizing coding practices.

For the Validation of Pep8 we use the [Code institute tester](https://pep8ci.herokuapp.com/) you will have to check each .py file coping and passing to the tester and correction according, most common Results include:

![pep8test](/img/pep8.png)

```
E225 missing whitespace around operator
E113 unexpected indentation
E501 line too long (82 > 79 characters)
```

A good result should have the message "All clear, no errors found."

#### Automated Testing

To use the Automated Testing we  have create some test in tests.py. To run the Python tests use the following command:

```
python manage.py test
```

If the test work as plan you will have a Ok from the System.

![Teste Image](/img/testinpy.png)

## Credits and Contact

The base.html

was take as exemple the one provide in during the Blog run creation and adapt.
