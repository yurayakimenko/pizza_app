# Pizza Constructor Django Example App

**This project is written with Django 2.1.7.**

You can view a working version of this app
[here](http://104.248.137.143:8000).
Running this app on your local machine in development will work as
well.

## Building

You can simply run:
```sh
$ git clone https://github.com/yurayakimenko/pizza_app.git
$ cd pizza_app
$ ./deploy.sh
```

Or do it hard way:

```sh
$ git clone https://github.com/yurayakimenko/pizza_app.git
$ cd pizza_app
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt

Before running the server you should provide Gmail secrets to `pizza_app/secrets.py`:
```python
EMAIL_HOST_USER = "example@gmail.com"
EMAIL_HOST_PASSWORD = "password"
EMAIL_ENABLE = True
```

Then you can:
```
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

Then visit `http://localhost:8000` to view the app.

