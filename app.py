from flask import Flask, request, jsonify
from rediscluster import RedisCluster

# Création de l'application Flask
app = Flask(__name__)

# Configuration des nœuds Redis dans le cluster
startup_nodes = [
    {"host": "173.17.0.2", "port": "7000"},
    {"host": "173.17.0.3", "port": "7001"},
    {"host": "173.17.0.4", "port": "7002"}
]

# Connexion au cluster Redis
client = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)

# Route pour ajouter un nouvel employé
@app.route('/employes', methods=['POST'])
def ajouter_employe():
    # Récupérer les données JSON de la requête
    data = request.json
    nom = data.get('nom')
    poste = data.get('poste')
    age = data.get('age')

    # Générer un nouvel ID pour l'employé
    id_employe = client.incr('employeIdCounter')

    # Enregistrer les informations de l'employé dans Redis
    employe_key = f'employe:{id_employe}'
    client.hmset(employe_key, {'nom': nom, 'poste': poste, 'age': age})

    # Réponse JSON
    response = {
        'message': 'Nouvel employé ajouté avec succès !',
        'employeId': id_employe
    }
    return jsonify(response), 201

# Route pour ajouter un nouvel utilisateur
@app.route('/utilisateurs', methods=['POST'])
def ajouter_utilisateur():
    # Récupérer les données JSON de la requête
    data = request.json
    username = data.get('username')
    email = data.get('email')

    # Générer un nouvel ID pour l'utilisateur
    id_utilisateur = client.incr('utilisateurIdCounter')

    # Enregistrer les informations de l'utilisateur dans Redis
    utilisateur_key = f'utilisateur:{id_utilisateur}'
    client.hmset(utilisateur_key, {'username': username, 'email': email})

    # Réponse JSON
    response = {
        'message': 'Nouvel utilisateur ajouté avec succès !',
        'userId': id_utilisateur
    }
    return jsonify(response), 201

# Point d'entrée de l'application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
