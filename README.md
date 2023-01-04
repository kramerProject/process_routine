# Objective

Extract data from a txt file containing purchase information concerning a fictious store. After data is parsed and validated It should be persisted in a sql data base.

# Requirements

- [X] Parse data

- [X] Validate

- [X] Persist in a sql data base


# Instructions

In order to run the app you should have [docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/install/) installed

1. Clone repo:

```
git clone git@github.com:kramerProject/process_routine.git

cd process_routine
```


2. Build the container:

```
make image
```

3. Get inside the container

```
docker exec -it process_routine bash
```

4. Start the app

```
python3 ./src/app.py
```
5. Check data on the database

```
docker exec -it mysqldb bash
```
```
mysql -uroot -p
```
```
type the password
```
```
show databases;
```

```
use teste;
```
```
select * from purchases;
```

# Tests

if your not on container RUN
```
docker exec -it process_routine bash
```
then RUN
```
cd src
python -m unittest parser_tests.py
```