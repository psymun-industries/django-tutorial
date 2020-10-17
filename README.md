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
As you can see, the Python module ```manage.py``` is essentially God, importing all the tools to manage the entire project. Hence the name, I suppose. In contrast, ```mysite/settings.py``` (which we'll see later) takes on the role the apostles, to whom we, being like Jesus, propagate God's wishes, in the hope that they will be carried out in the way God (```manage.py```) intends. When the project contains more than one app, we can think of these as multiple universes, each with its own Jesus and his apostles, but all under one God.

 Hopefully that clears up any confusion at this early stage. 

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

## [Part 2](https://docs.djangoproject.com/en/3.1/intro/tutorial02/)
Time for a quick chat with the apostles via the app's ```settings.py```. I changed ```LANGUAGE_CODE``` to ```'en-gb'``` because that's what I speak, and left the time zone as UTC because that's my time. Maybe it even works out local daylight savings, who knows. 

### First DB migration
Django comes with a load of cool models and templates built in, plus an excellent site admin facility, so there's already a DB migration to be done before we've written any models. We'll do what the pros tell us:
```python
python manage.py migrate # And God said "Let there be a table for each of my models"
```
### Models
Now that God's happy, we can make some models of our own. We are Jesus after all, so we can morph into God ourselves if we so choose, and do all the stuff God can.

We define the Python classes ```Question``` and ```Choice```. These are automatically mapped to database models with the fields we define. The ```django.db.models``` module handles all of this for us: our models inherit from the base ```Model``` class and use all field types defined for us beforehand. Who said OO was shit!?

Once we've invented the models we need to meet the apostles again and let them know their universe has changed. We do this by registering the app in ```mysite/settings.py``` which basically makes the ```polls``` universe aware of itself and the models it contains. 

The docs then go on to describe the DB migrations in detail. If you're happy with that, the quick way out is 
```python
python manage.py makemigrations
python manage.py migrate
```

### Further sculpting our models
We add ```__str__()``` methods to our models so they identify themselves in a readable way when called upon by the system. Those familiar with Python will recognize its special double-underscore methods. Those who are not will soon grow to love them and their weird, hard-to-type syntax. 

We also add ```datetime``` functionality to the ```Question``` model by way of a ```pub_date``` field and the ```was_published_recently()``` method which returns whether or not the ```Question``` was incarnated within the last day. 

At this point, we open up God's sandbox and create instances of his great models. I opened up a REPL shell and created thus:
```
(.env) ~/dev/repos/django-tutorial/mysite$ python manage.py shell
Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from polls.models import Choice, Question
>>> from django.utils import timezone
>>> q = Question(question_text="Where am I?", pub_date=timezone.now())
>>> q.save()
>>> q.question_text
'Where am I?'
>>> q.choice_set.create(choice_text="Outer space", votes=0)
<Choice: Outer space>
>>> q.choice_set.create(choice_text="Hell", votes=0)
<Choice: Hell>
>>> q.choice_set.create(choice_text="The lavatory", votes=0)
<Choice: The lavatory>
>>> q.choice_set.all()
<QuerySet [<Choice: Outer space>, <Choice: Hell>, <Choice: The lavatory>]>
>>> exit()
```