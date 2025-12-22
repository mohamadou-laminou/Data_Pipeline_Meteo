import requests
import config
import mysql.connector
from datetime import datetime

def meteo () :
    # Je me connecte à mon sql, vous pourvez mettre vos identifiants de connexion à la place des miennes
    conn = mysql.connector.connect(
        host = config.DB_HOST, # Modifiez ceci
        user = config.DB_USER, # Modifiez ceci
        password = config.DB_PASSWORD, # Modifiez ceci
        database = config.DB_NAME # Modifiez ceci
    )
    cursor = conn.cursor()

    villes= ["Montpellier", "Paris", "Yaounde", "Maroua", "Quebec"] # Vous pourvez Modifier les villes ici
      # Vous devez modifier l'API  à "appid=" vous pouvez aussi modifier la metric et la langue à "lang="
    for ville in villes :
        url =f"http://api.openweathermap.org/data/2.5/weather?q={ville}&appid={config.API_KEY}&units=metric&lang=fr"

        reponse = requests.get(url)

        if reponse.status_code == 200 :

            data=reponse.json()

            temp = data ['main']['temp']
            pressure = data ['main']['pressure']
            vent = data ['wind']['speed']
            desc = data ['weather'][0]['description']
            humidity = data['main']['humidity']
            date_now = datetime.now()

            print (f"{ville}")
            print (f"Temperature : {temp} °C")
            print (f"Pressure : {pressure} hPa")
            print (f"humidité : {humidity}%")
            print (f"Vent : {vent} m/s")
            print (f"Description : {desc}")
            print ("-_-_-_-_-_-_-_-")

            # Vous devez également modifier ces infos en fonction du nom des colonnes de votre base de données

            sql =""" INSERT INTO meteo_data (ville, date_releve, temperature, humidite, pression, vitesse_vent, description) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
            valeurs = (ville, date_now, temp, humidity, pressure, vent, desc)  # On fait correspondre les données du haut avec leur nom dans python

            cursor.execute(sql,valeurs)
            conn.commit()

        elif reponse.status_code == 401 or reponse.status_code == 404 :
             print (f"erreur avec la ville: {ville} code : {reponse.status_code}")
    cursor.close()
    conn.close()        

if __name__ == "__main__" :
    meteo()     


                                      # Merci, cher data mate
