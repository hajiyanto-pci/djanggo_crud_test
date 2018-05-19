# Test programming 

This is simple project CRUD books using framework django

# Running the Application

- install django on ubuntu :
  $ sudo apt-get install pip
  $ sudo pip install django

- Before running the application we need to create the needed DB tables:
  python3 manage.py migrate

- now you can run the development web server:
   python3 manage.py runserver
  To access the applications go to the URL <http://localhost:8000/>


# I need a user and password to access "books\_fbv\_user"

Yes, the "book" demonstrate how CRUD can work with Django users, and you do
need to create a user to test it, you can create a user using the following command:

    python3 manage.py createsuperuser

To create a normal user (non super user), you must login to the admin page and
create it: <http://localhost:8000/admin/>