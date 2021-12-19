pushd %CD%\django_app_component
REM start http://localhost:8080/TODO/Django_works/
REM python manage.py runserver localhost:8080
start http://192.168.10.100:8080/TODO/Django_works/
python manage.py runserver 192.168.10.100:8080