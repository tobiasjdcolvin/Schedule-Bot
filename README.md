**Setup instructions:**

1. Clone repository with git clone
2. ***Mac:*** python3 -m venv .venv  ***Windows:*** python -m venv .venv
3. ***Mac:*** source .venv/bin/activate  ***Windows:*** .venv/Scripts/Activate.ps1
4. ***Mac:*** python3 -m pip install django~=5.0.0  ***Windows:*** python -m pip install django~=5.0.0
5. ***Mac:*** python3 -m pip install requests  ***Windows:*** python -m pip install requests
6. ***Mac:*** python3 manage.py migrate  ***Windows:*** python manage.py migrate
7. ***Mac:*** python3 manage.py createsuperuser  ***Windows:*** python manage.py createsuperuser
8. ***Mac:*** python3 manage.py runserver  ***Windows:*** python manage.py runserver

Now that you are setup, you can always go back into the virtual environment with: ***Mac:*** source .venv/bin/activate  ***Windows:*** .venv/Scripts/Activate.ps1
and deactivate the environment with the *deactivate* command. Running the development server is as simple as being inside the virtual environment and doing: ***Mac:*** python3 manage.py runserver  ***Windows:*** python manage.py runserver.

Some useful commands to remember: *manage.py makemigrations* *manage.py migrate* 
