import requests

# la liste des villes avec leur coordonner
villes = {
    "Nanterre": [48.89, 2.20],
    "Paris": [48.8566, 2.3522],
}

def recuperer_meteo(latitude, longitude):
    # on utilise API pour récupérer la meteo actuelle avec la latitude et la longitude
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    
    response = requests.get(url)

    if response.status_code == 200:
        donnees = response.json() 
        temperature = donnees['current_weather']['temperature']  # recuperation de la temperature
        vent = donnees['current_weather']['windspeed']  # recuperation de la vitesse du vent
        return temperature, vent
    else:
         # la réponse de API a une erreur
        print("Erreur...")
        return None, None

# while permet de creer un menu  
while True:
    # le menu
    print("\nMenu Météo:")
    print("1. Météo à Nanterre")
    print("2. Ajouter une ville et voir sa météo")
    print("3. Afficher météo pour toutes les villes")
    print("4. Quitter")
    
    choix = input("Votre choix: ")
    
    if choix == "1":
        # on recupere les coordonner de Nanterre
        coords = villes["Nanterre"]
        # on recupere la temperature et le vent
        temp, vent = recuperer_meteo(coords[0], coords[1])
        print(f"meteo à Nanterre : temperature {temp}°C, vent {vent} km/h")
        
    elif choix == "2":
        # on demande le nom et les coordonnées de la nouvelle ville
        nom = input("Nom de la ville: ")
        lat = float(input("Latitude: "))
        lon = float(input("Longitude: "))
        # on ajoute la ville à notre liste
        villes[nom] = [lat, lon]
        # on récupère la météo pour cette ville
        temp, vent = recuperer_meteo(lat, lon)
        print(f"meteo à {nom} : temperature {temp}°C, vent {vent} km/h")
        
    elif choix == "3":
        # on parcourt toutes les ville et on affiche leur meteo
        for ville, coords in villes.items():
            temp, vent = recuperer_meteo(coords[0], coords[1])
            print(f"{ville} : temperature {temp}°C, vent {vent} km/h")
            
    elif choix == "4":
        # stop le script
        print("Bye")
        break
        
    else:
        # Si l'utilisateur entre un choix invalide
        print("merci de mettre un vrai choix")
