image:
	docker-compose up

stop:
	docker-compose stop
	
cleanup: stop
	docker-compose rm -f -v

run_sql:
	docker exec -it mysqldb bash

see_sql_infos:
	docker inspect mysqldb

run_pr_container:
	docker exec -it process_routine bash



# python -m unittest ./src/parser_tests.py