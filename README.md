#### gobd.delivery is a simple delivery management application.
#### seller can create profile and place delivery requests.
#### a seller can cancel orders which not yet accepted by a delivery boy.
#### a seller can view all order list and their status on dashboard.
#### delivery boy can Accept New Tasks from store.
#### delivery boy can reject his/her task once accepted.
#### delivery boy can view all his Past accepted tasks and completed tasks on dashboard.
#### delivery boy can only accpet three tasks in his account if he accept more he/she needs to perform action on old tasks.
#### Setting up

setup Virtual Environment
```sh
$ virtualenv venv (creates new virtualenv for project)
$ source venv/bin/activate (activate virtualenv assumeing using ubuntu)
$ pip3 install -r requirements/  (install dependencies)
```

create migrations, create tables in db, and create a superuser to have the dashboards.

```sh
$ python3 manage.py makemigrations (creates migration files based on your models)
$ python3 manage.py migrate (creates the tables in your db based on the migration files)
$ python3 manage.py createsuperuser (creates a superuser for your application in the db)
$ python3 manage.py runserver (run server)
```


### for frontend ###

  
- Make sure to have python3, pip3 and virtual environment installed on your system
- Install all dependencies using command `pip install -r requirements/local.txt`
- Create database and run migrations using command `python manage.py migrate`

You can refer to django-cookiecutter project's [
](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html) for more detailed steps.

Follow below steps to setup frontend related stuff (Live reloading, SASS compilation, etc):
  
 - Make sure to have node and npm installed on your system
 - Install node and npm on your system
 - Install gulp globally using command `npm install -g gulp-cli` & `npm install -g gulp`
 - Install local dependencies using command `npm install`
 - Now you can just run command `gulp` to start server with live reloading and saas compilation enabled.


**Following are the available commands:**
 - `gulp` - The base app will run as it would with the usual `manage.py  runserver` but with live reloading and Sass compilation enabled. When changing your Sass files, they will be automatically recompiled and change will be reflected in your browser without refreshing.
 -  `python manage.py createsuperuser` - create a superuser
 - `pytest` - Runs tests with py.test
 - `coverage run -m pytest & coverage html  & open htmlcov/index.html` - Runs tests and check for coverage
 
 
 
 check list 



 - dashboard 2 (2)
# - account update form store & rider (2)
# - auth password missmatch report(2) 
 - django admin graph/ features (3)
 - crm (3)
 - scrolling (4)
 - {% if user.is_authenticated %} loop to sign up

 - favicon, header, MVT revision(4)
# - footer correction (4)
# - seller payment- sum it to template
# - runsheet (1)
# - payroll (5)





    
    
    

 
 