# Pizza Constructor Django Example App

**This project is written with Django 2.1.7.**

You can view a working version of this app
[here](http://193.124.176.237:8000).
Credentials for `/admin`:
```
login: root
password: 1q2w3e4r5t6y
```
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
```

Before running the server you should provide Gmail secrets 
to `pizza_app/secrets.py`:
```python
EMAIL_HOST_USER = "example@gmail.com"
EMAIL_HOST_PASSWORD = "password"
EMAIL_ENABLE = True
```

Also you should let [less secure 
apps](https://support.google.com/accounts/answer/6010255?hl=en)
access your account.

Then you can:
```sh
$ python manage.py migrate
$ python manage.py init_db
$ python manage.py createsuperuser
$ python manage.py runserver
```

`init_db` will create custom ingredient's groups and ingredients itself 
with random prices. You can change names in 
`pizza_constructor/management/commands/init_db.py`

Then visit `http://localhost:8000` to view the app.

