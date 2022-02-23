# Start Project with Docker

- Clone Repository with git clone

- create enviroment with the command " python3 -m venv env "

- in the folder env/ create file with name ".env" and in the file add two Variables (USER_DB = 'xxxx' and PASSWORD_DB = 'xxxx')

- later execute the command "docker-compose up --build --force-recreate" for install dependencies and run project

- Execute the command " docker-compose run web python manage.py makemigrations " 

- and the command " docker-compose run web python manage.py migrate "

- for execute project in future use the command "docker-compose up" 