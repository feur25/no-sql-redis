### Lancement du docker redis

1. Télécharger le projet `$ git clone hhttps://github.com/feur25/no-sql-redis`
2. `docker-compose build`
3. `docker-compose up` ou `docker-compose up -d`


docker exec -it docker-redis-cluster-redis1-1 redis-cli -c -h 173.17.0.2 -p 7000


SET employe:1 '{"nom": "John Doe", "poste": "Développeur", "age": 30}'

GET employe:1
