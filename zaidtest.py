import pandas as pd
import csv
import folium
from flask import Flask, render_template,jsonify, request
from json import loads,dumps



def fuctiepointerinfo(zoektekst):
    bestand = pd.read_csv("csvfiles/MuseaGalleries.csv", sep=";", encoding='latin-1')
    resultaat = bestand[bestand['Title'].str.contains(zoektekst, case=False, na=False)][['Title', 'Adres']].iloc[0]
    return resultaat

def functiemap():
    return render_template('museum_map.html')

def functiezaid3zoek():
    zoeknaam = request.args.get('naam', '')
    bestand = pd.read_csv("csvfiles/MuseaGalleries.csv", sep=";", encoding='latin-1')
    geselecteerde_kolommen = ['Title', 'Shortdescription', 'Calendarsummary', 'City', 'Adres', 'Zipcode']
    resultaat = bestand[bestand['Title'].str.contains(zoeknaam, case=False)][geselecteerde_kolommen]
    resultaat_lijst = resultaat.to_dict(orient='records')

    return jsonify(resultaat_lijst)


def functiemaakmap():
   keys = ('Latitude','Longitude')
   records = [ ]

   bestand = pd.read_csv("csvfiles/MuseaGalleries.csv", sep=";", encoding='latin-1')
   #print(bestand)
   data = bestand.to_dict(orient='records')
   museum_map = folium.Map(location=[52.377956, 4.897070], zoom_start=15)

   for row in data: 
        records.append({key: row[key] for key in keys})
        latitude = float(row['Latitude'].replace(',', '.'))
        longitude = float(row['Longitude'].replace(',', '.'))

        #print(records[0])
        NaamLocatie = row['Title']
        Adress = row['Adres']
        

        tooltip = f'{NaamLocatie}, {Adress}'

        folium.Marker([latitude, longitude], tooltip=tooltip).add_to(museum_map)
        museum_map.save('museum_map.html') 


def functie_zoek_locatie_in_CSV(invoer):
    
    keywords = [invoer]
    matched_rows = [ ]    

    BestandCSV = pd.read_csv("csvfiles/MuseaGalleries.csv", sep=";", encoding='latin-1')
   
   
    for index,row in BestandCSV.iterrows(): 
     
        title = str(row.get("Title", "")).lower()
        Short_description = str(row.get("Shortdescription", "")).lower()
       
        

        if any(keyword in title or keyword in Short_description for keyword in keywords):
            matched_rows.append(index)
        
    if not matched_rows:
            print("\nNo matching rows found.")
            return "[]"
        
    results_dataframe = BestandCSV.loc[matched_rows].copy() 

    result = results_dataframe.to_json(orient="records")
   

    return result
    



