virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
touch pizza_app/secret.py
echo 'EMAIL_HOST_USER = "example@gmail.com"
EMAIL_HOST_PASSWORD = "password"
EMAIL_ENABLE = False' >> pizza_app/secret.py
python manage.py migrate
python manage.py runserver
