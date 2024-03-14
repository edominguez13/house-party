# house-party

## About

This is a guided project based on the playlist [Django & React - Full Stack Web App Tutorial](https://www.youtube.com/playlist?list=PLzMcBGfZo4-kCLWnGmK0jUBmGLaJxvi4j) of Mar 7, 2021.

The goal is to create a collaborative music playing system where users can interact and manipulate what music is playing.

The host will create a room and the guest will receive a code that will allow them to control the music, vote to skip the song, stop, play, etc.

### Note

This is a 3 year old project that I seached to do step by step and cement my knowledge of React and Django.

I took the liberty of doing somethings my way based on the current best practices. For example: creating a virtual environment for the Django project.


## Project setup

### VS Code

Download Visual Studio Code IDE and the following extensions:

- Prettier - Code formatter
- Python
- Django
- ES7 React/Redux/GraphQL/React-Native
- JavaScript (ES6) code snippets

### Installing Django and Django Rest Framework (DRF)

Steps I took for installing the Django and DRF:

1. Checked the versions of pip and Python running the following commands:
```
// terminal
pip --version /* Checks the current version of pip */
python --version /* Checks the current version of python */
py -m pip install --upgrade pip /* updates pip *
```
2. Before creating the virtual environment, deleted the possible source of conflicts:
```
// terminal
pip uninstall virtualenv /* to avoid conflicts with pipenv */
pip uninstall pipenv /* to be sure we have a clean slate */
```
3. Install pipenv:
```
// terminal
pip install pipenv
```
4. Create a project folder:
```
// terminal
mkdir back-end /* I called it 'back-end' */
```
5. Install virtual env and Django inside the 'back-end' folder:
```
// terminal
cd back-end
py -m pipenv install django
```
6. Select the Python interpreter for the virtual env:

    1. Access 'Python: select interpreter' by pressing Ctrl + Shift + P.
    2. Click on 'Python: select interpreter'.
    3. Select the option with the forder name, in this case:
        > Python 3.12.1 ('back-end-DQf-JtYg')

        This will allow you to use the virtual env without having to use the commands `pipenv shell` to start it and `exit` to close it.
    4. Close the terminal and reopen it to see the change.


7. Create the Django project:

    The following code will create a Django project folder named 'music_controller' with a Django App folder inside with the same name.
```
// terminal
django-admin startproject music_controller /* the name given by the youtube teacher */
```
8. Install DRF:
```
py -m pip install djangorestframework
```
9. Define 'rest_framework' as an INSTALLED_APP in the settings.py file inside the Django project folder or like I like to call it the "Django default app project":
```
// back-end\music_controller\music_controller\settings.py

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',                 # here
]

```

## The first api of the project

### Creating the first api

1. Create an app that will serve as an API with the following command:
```
// terminal

py manage.py startapp api /* the last word 'api' is the name of the API */
```
2. Define the new App inside of settings.py:
```
// back-end\music_controller\music_controller\settings.py

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',                        # here
]
```
3. Create a *view* inside of the 'api' App to test the server:

    Keep in mind that *views* are what render what we see in the *end points*.

    *End poinds* are site locations of a website, like: /index, /login, etc.
```
// back-end\music_controller\api\views.py

from django.shortcuts import render
from django.http import HttpResponse # imported

# Create your views here.
def main(request):
    return HttpResponse("Hello")
```

4. Create the *urls.py* file inside the 'api' App folder.

    This file stores all *url endpoints* local to this App.

```
// back-end\music_controller\api\urls.py

from django.urls import path
from .views import main # from the same folder's views file import the function 'main'

urlpatterns = [
    path('', main),
]
```
5. Define the *url path* of the 'api' inside the Django project folder's *urls.py* file.

    If the first argument (or route property) of the path function is an empty string, then the *end point* will be blank.

    In the code block below, if the website domain is example.com, the defined *end points* will be:

        - example.com/admin
        - example.com/

```
// back-end\music_controller\music_controller\urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),       #this one
]
```
6. Make migrations:

    This is done at the beginning or when we modify the models and database.

```
// terminal

py manage.py makemigrations
py manage.py migrate
```
7. Run the webserver:
```
// terminal

py manage.py runserver
```