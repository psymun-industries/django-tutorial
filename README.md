# django-tutorial
The official djangoproject.com tutorial, ```venv```ed and ```git```ified for your delectation

## What's this?
This is the [tutorial from Django's documentation](https://docs.djangoproject.com/en/3.1/intro/tutorial01/), using the newest version of the package, at the time of writing: 3.1.2. It's set up from the perspective of someone using a Debian/Ubuntu sort of system. 

## Why?
Django is great, but it farts out a lot of files into a non-trivial directory structure which might be intimidating if you're new. I thought it might be helpful for myself and maybe even others to have the various stages of the tutorial committed in (more-or-less) order of presentation. 

## Oh.
Yes. 

## Virtual Environment Setup
First make sure that Python 3.6 or greater is available on your path. I'm using 3.8.5. Clone the repo and `cd` in. Then, if you're missing any of the following:
```bash
sudo apt install -y python3-pip python3-venv
```
I also highly recommend installing the ```tree``` package if you don't have it to hand so you can visualize the directory structure of the project more easily, and in line with how it's presented in the Django documentation. 

The following commands install and activate a virtual environment so version changes in the system Python installation won't affect the project. You might have already pointed ```python``` to your preferred version of Python 3, in which case ```python3``` below should just be ```python```. 
```bash
python3 -m venv .env 
source .env/bin/activate # sets environment vars in your terminal
```
The links ```pip``` and ```python``` are now pointing to the appropriate versions for the project within the ```venv```. So we can just run: 
```bash
pip install -r requirements.txt
```
When you've had enough of the environment and want to go home:
```bash
deactivate
```
will unset the `venv` variables and return you to your normal terminal just like the good old days. Anyway, with the environment running, you can now follow along. If you like, delete all the project files with 
```bash
rm -r mysite/
```

and make them as we go. It will be so much fun. 

#
# The tutorial
## [Part 1](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)
### Create the project
From the root directory of the repo, ensure you're in the magical dreamworld of the virtual environment, and run:
```python
django-admin startproject mysite
```
You can run ```cd mysite/ && tree``` to check that the generated files look like the Docs say they should. Hopefully 
```python
python manage.py runserver
```
works for you as it should. If it does, crack open a beer. If it doesn't, definitely still crack open a beer. 

### Create an app
The docs now tell us to magically make an app happen out of thin air, so do:
```python
python manage.py startapp polls
tree # I just love printing trees
```
Look at all those files, are they all for me!?
```bash
.
├── db.sqlite3
├── manage.py
├── mysite
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── settings.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   └── wsgi.cpython-38.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── polls
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
```
As you can see, the Python module ```manage.py``` is essentially God from the application's perspective, containing lots of tools to manage the entire project. Hence the name, I suppose. In contrast, ```mysite/settings.py``` (which we'll see later) is like the apostles, to whom we, being like Jesus, proselytize God's instructions in a rather disparate and convulted way, in the hope that they will be carried out in the way God (```settings.py```) intends. Hopefully that clears up any confusion at this early stage. 

### First view
Anyway, next we create ```polls/views.py``` as shown. We define a function ```index()``` which takes an HTTP request as a parameter and returns an ```HttpResponse``` object. As you can imagine, this response eventually gets fed to the client browser.

The next bit is potentially confusing. We'll create two files called ```urls.py```, one in the application root, ```mysite/polls/``` and one in the project root, ```mysite/```. 

The former ```mysite/poll/urls.py``` maps the output of ```index()```, an ```HttpRespose```, to a blank (root) URL from the perspective of the ```polls``` application. 

The latter ```mysite/urls.py``` maps any URLs defined in our ``polls`` app to the URL ```polls/``` from the perspective of the entire project. So the views defined in ```polls``` are all under the URL ```polls/```. 

Wonderful. Now's the time to 

```python
python manage.py runserver
```
and visit http://localhost:8000/polls which will hopefully yield an actual VIEW! Time for a beer I reckon. 
 