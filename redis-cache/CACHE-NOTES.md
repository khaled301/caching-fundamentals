## Important resources
    - https://docs.vultr.com/how-to-cache-mysql-data-with-redis-and-python-on-ubuntu-20-04

## Basic standalone Requirements
Verify the available Python3 version on your server.

> python3 -V
Update the server.

> sudo apt update
Install the python3-pip package.

> sudo apt install -y python3-pip
Install the MySQL connection driver.

> pip install mysql-connector-python
Install the redis library.

> pip install redis

### to run redis and redis-cli using docker compose
> docker compose run redis redis-cli -h redis -a <your_secret> -n 0

### Get into MySQL DB

> mysql -u<MySQL_USER> -p<MySQL_PASS>

### Run a SQL scripts from command line in [Bash Terminal]

> mysql -u<MySQL_USER> -p<MySQL_PASS> < init.sql

### Get users list from MySQL
> select host, user from mysql.user;