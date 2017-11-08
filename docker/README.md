# Running TerminalRoastDB using Docker
TerminalRoastDB can be run using a Docker Compose project. The project consists of 2 containers: one to run the MySQL database and another one to run the python server. Copy `docker-compose.yml.example` to the root of the repository and run `docker-compose up` to get going.


from the repository root:
```
cp docker/docker-compose.yml.example docker-compose.yml
docker-compose up
```
Let docker run in the foreground. Messages from the python server and the MySQL database log here.

To run a roast open a new terminal and exec into the container. (TODO write wrapper for this) Then run the roast.

```
docker-compose exec terminalroast_python bash
cd cmds
python3.5 Roaster_Run_Recipe.py 2
```

Connect to TCP port 3306 on the host to connect to the MySQL database inside the running database container. You can also exec into the database container to poke around:

```
docker-compose exec terminalroast_mysql
mysql -hlocalhost -uterminalroaster -pterminalroasterpasswd terminalroastDB
```
