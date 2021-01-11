# ProjectChallenge.io-api

test commit

2021/01/11 
* set up directory on my machine - interacts with git clone, git add, git commit, git push 
* download vitualenv `sudo pip3 install virtualenv` to set up virtual environment for projects including Flask 
* activate venv `. venv/bin/activate` deactivate `deactivate`
* vscode extensions Atom dark theme and python
* download Insomnia to test api (get and post request)
* set up ssh keys and ssh agent and put it into github to avoid entering credentials every time
* download docker image for postgres `docker pull postgres:alpine` (alpine version)
* run docker image as a container by `docker run  -p 5432:5432 --name projectchallengedb -e POSTGRES_PASSWORD=projectchallengedb postgres:alpine` 
* use docker-compose with `docker-compose up` to start server and `docker-compose down` to stop server 
* download pgadmin 4 to visual and update the database, create server with credentials
* we can also access the database by going inside the running container by `docker exec -it CONTAINER_ID bash`, we can `psql --username=projectchallengedb` to connect with the database, and then we can run queries, `\d` to see all tables/relations
* download `psycopg2` package to establish connection with the database from our api 
* write db_config.py to give access to databse information such as user, password, name and host
* wirte connect(), get_user(), db_to_dict()
