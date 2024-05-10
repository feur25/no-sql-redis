### Lancement du docker redis

1. Télécharger le projet `$ git clone https://github.com/feur25/no-sql-redis`
<img width="219" alt="Capture d’écran 2024-05-10 à 10 18 09" src="https://github.com/feur25/no-sql-redis/assets/39668417/cbeca091-2e74-446c-a064-1ed3c4855737">

2. `docker-compose build`
3. `docker-compose up` ou `docker-compose up -d`

<img width="583" alt="Capture d’écran 2024-05-10 à 10 17 50" src="https://github.com/feur25/no-sql-redis/assets/39668417/11eb0530-5cc1-4438-bf16-777f8d776798">


  docker exec -it docker-redis-cluster-redis1-1 redis-cli -c -h 173.17.0.2 -p 7000


  SET employe:1 '{"nom": "John Doe", "poste": "Développeur", "age": 30}'

  GET employe:1

<img width="583" alt="Capture d’écran 2024-05-10 à 10 17 25" src="https://github.com/feur25/no-sql-redis/assets/39668417/e1d85fae-8691-4b4a-8a8d-c2f0cf00a86c">

