# Objective

Extract data from a txt file containing purchase information concerning a fictious store. After data is parsed and valid It should be persisted in a sql data base.

# Requirements

- [X] Parse data

- [X] Validate

- [X] Persist in a sql data base


# Instructions 

You should have docker and docker-compose installed

1. Clone repo:

```
git clone git@github.com:kramerProject/candidate_scraper.git

cd candidate_scraper
```


2. Criar e ativar um ambiente virtual e instalar as dependências do projeto:

```
python3 -m venv .venv

source .venv/bin/activate

pip3 install scrapy mysql-connector-python
```

3. Configurar variáveis de ambiente

```
export MYSQL_USER='seu user name'

export MYSQL_PASSWORD='sua senha_mysql'

export MYSQL_HOST=localhost
```

4. Criar o banco de dados mysql

```
DROP DATABASE IF EXISTS candidates;

CREATE DATABASE IF NOT EXISTS candidates;
```
5. Rodar o serviço

```
cd src

scrapy crawl ap
```

# Testes

```
python -m unittest tests/test_scraper.py
```
# Resultados

- Tempo do serviço: 34 minutos
- 46.707 itens salvos no banco de dados

![image Info](src/assets/scraper_stats.png "stats")





# Rodar o mysql

```
docker exec -it mysqldb bash
```
```
mysql -uroot -p
```
```
digitar o password
```
```
show databases;
```

```
use teste
```
```
select * from purchases;
```