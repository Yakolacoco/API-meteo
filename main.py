import requests

# la liste des ville
villes = {
    "Nanterre": [48.89, 2.20],
    "Paris": [48.8566, 2.3522],  
}

def recuperer_meteo(latitude, longitude):
    # on utilise API pour savoir la temperature de la ville avec latude et la longitude
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    
    # il va envoyer une requests
    response = requests.get(url)

    # pour avoir une reponse de API si on resoin il donne la reponse il passe a if si non sa passe vers else pour qui affiche erreur
    if response.status_code == 200:
        donnees = response.json()  
        temperature = donnees["current_weather"]["temperature"]  # on va prendre la temprature dans la liste 
        return temperature
    else:
        # si la requete sa marche 
        print("Erreur...")
        return None
    
 # while sa saire a faire une boucle avec des condition si la personne ne fait pas 3 
while True:
    #  le menu
    print("1 - Choisir une ville dans la liste")
    print("2 - Entrer une ville manuellement avec coordonnées")
    print("3 - Quitter")

    # on va demander le choix à l utilisateur
    choix = input("Votre choix : ")
     # option 1 : donne la liste des ville et utilisateur peut choisir la ville avec des chiffre 
    if choix == "1":
        for i, ville in enumerate(villes, 1):
            print(f"{i} - {ville}") # donne un numerro avec la ville 
        num = input("Choisissez une ville (numéro) : ")
        if num.isdigit() and 1 <= int(num) <= len(villes): # verifie si le numero est dans la liste 
            ville = list(villes)[int(num)-1] # choisie la ville avec le nimero 
            temp = recuperer_meteo(*villes[ville])  # va recuperer la temperature de la ville 
            if temp is not None:
                print(f"{ville} : {temp}°C") # affiche la ville avec sa temperature 
        else:
            print("Erreur merci de mettre un chiffre de la liste")

    # option 2 : donner le nom de la ville et les cordonner 
    elif choix == "2":
        ville = input("Entrez le nom de la ville : ")
        lat = input("Entrez la latitude : ")
        lon = input("Entrez la longitude : ")
        try:
            lat = float(lat)  # latitude 
            lon = float(lon)  # longitude
            temperature = recuperer_meteo(lat, lon)  # on recupere la temperature
            if temperature is not None:
                print(f"La température actuelle à {ville} est de {temperature}°C")
        except ValueError:
            # si c est pas des nombre sa mais erreur
            print("erreur merci de mettre des nombre correcte")

    # option 3 : on stop le script
    elif choix == "3":
        print("Bye")
        break 
