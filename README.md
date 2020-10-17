# django-tutorial
The official djangoproject.com tutorial, venv'd and gitified for your delectation

## What's this?
This is the [tutorial from Django's documentation](https://docs.djangoproject.com/en/3.1/intro/tutorial01/), using the newest version of the package at the time of writing, 3.1.2. It's set up from the perspective of someone using Debian/Ubuntu sort of thing. 

## Why?
Django is great but farts out a lot of files into a non-trivial directory structure which might be intimidating if you're new. I thought it might be helpful for myself and maybe even others to have the various stages of the tutorial committed in (more-or-less) order of presentation. 

## Oh.
Yes. 

## Virtual Environment Setup
First make sure that Python 3.6 or greater is available on your path. I'm using Clone the repo and `cd` in. Then, if you're missing any of the following:
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
will unset the `venv` variables and return you to your terminal as God intended. Anyway, with the environment running, you can now follow along. If you like, delete all the project files with 
```bash
rm -rf mysite/
```

and make them as we go. It will be so much fun. 

#
# The tutorial
## [Part 1](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)
From the root directory of the repo, ensure you're in the magical dreamworld of the virtual environment, and run:
```python
django-admin startproject mysite
```
You can run ```cd mysite/ && tree``` to check that the generated files look like the Docs say they should. Hopefully 
```python
python manage.py runserver
```
works for you as it should. If it does, crack open a beer. If it doesn't, definitely still crack open a beer. 