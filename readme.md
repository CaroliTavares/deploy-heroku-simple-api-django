- > Criando Projeto

$ python -m venv myvenv
$ myvenv\Scripts\activate
$ pip install Django
$ pip install djangorestframework
$ mkdir backend
$ cd backend
$ django-admin startproject backend .
$ django-admin startapp api
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser

- > Fazendo Deploy  de api simples no Heroku

$ heroku login -i
$ heroku git:remote -a <nome criado no site do heroku>
$ git init
$ git add .
$ git commit -m "deploy"
$ git push -u heroku main
$ heroku run python manage.py migrate
$ heroku run python manage.py create superuser


