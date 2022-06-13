pip install virtualenv
virtualenv pawnshop_env
source course/bin/activate

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate