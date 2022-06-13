pip install virtualenv
virtualenv pawnshop_env
.\pawnshop_env\Scripts\activate

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations
python manage.py migrate


