This is a pre-interview coding test from Incling.

To start the server type:

python manage.py migrate
python manage.py runserver

To create a super user ( staff member ):

python manage.py createsuperuser

To visit the admin page go to:

http://localhost:8000/admin/

To see the api documentation go to:

http://localhost:8000/api/docs/

Current APIs:

Task API - http://localhost:8000/api/task/

Tiles API - http://localhost:8000/api/task/

User API - http://localhost:8000/api/user/

Description:

Users can be created using the post method. Upon creation,
users would be authenticated.
To view other users user the get method.
