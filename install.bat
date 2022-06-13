pip install virtualenv
virtualenv pawnshop_env
.\course\Scripts\activate

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
