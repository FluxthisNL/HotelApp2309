import keyword
import pandas as pd
from json import loads,dumps
import matplotlib.pyplot as plt
from flask import render_template, jsonify, request

def search_csv_for_keywords(invoer):
    try:
        
    #Het CSV bestand lezen en in een DataFrame stoppen
        
        bestand = pd.read_csv("csvfiles/TA_restaurants_curated.csv")
        lijstid = []
        
    #De gebruiker prompten om keywords in te vullen
    
        keywords_input = invoer.lower()
        search_keywords = [keyword.strip() for keyword in keywords_input.split(",")]
        
    #Lege DataFrame maken om de rijen op te slaan
    
        results_dataframe = pd.DataFrame(columns=bestand.columns)
        
    #Door de dataframe heen loopen op zoek naar keywords in cuisine styles en cities
        for index, row in bestand.iterrows():
            city= str(row.get("City", "")).lower()
            cuisine_style = str(row.get("Cuisine Style", "")).lower()
            
            if all(keyword in city or keyword in cuisine_style for keyword in search_keywords):
                lijstid.append(index)
        results_dataframe = bestand.loc[lijstid].copy()
            
    #rijen weergeven
        if not results_dataframe.empty:
            print("\nMatching Rows:")
            print(results_dataframe)
        else:
                print("\nNo matching rows found.")
                
    #error handling            
    except FileNotFoundError:
       print(f"Error: the file '{csv_file} does not exist'")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
                
    result = results_dataframe.to_json(orient="records")
    parsed = loads(result)
    return dumps(parsed, indent=4)  

def restaurantNumbers(rating_treshold=4.0):

  bestand = pd.read_csv("csvfiles/TA_restaurants_curated.csv")

  highly_rated_restaurants= bestand[bestand["Rating"] > rating_treshold]

  city_counts = highly_rated_restaurants["City"].value_counts()

  city_info = pd.DataFrame({"RestaurantCount":city_counts})

  city_reviews = highly_rated_restaurants.groupby("City")["Number of Reviews"].sum()

  city_info["TotalReviews"] = city_info.index.map(city_reviews)

  city_info["TotalReviews"] = city_info["TotalReviews"]

  city_info_dict = city_info.to_dict(orient="index")
  
  return jsonify({"city_info_dict": city_info_dict})
  
def filter_and_dropdown(price_range):
    
    #csv bestand lezen
    df= pd.read_csv("csvfiles/TA_restaurants_curated.csv")
    
    #Amsterdam als stad filteren
    amsterdam_restaurants = df[df["City"] == "Amsterdam"]
    
    #Lege lijst voor index
    legelijst_prijs = []
    
    #Loopen door amsterdam_restaurants voor alle prijs indicaties
    for i, ad in amsterdam_restaurants.iterrows():
        if str(ad["Price Range"]) == price_range:
            legelijst_prijs.append(i)
    
    leegDataframe = df.loc[legelijst_prijs].copy()
    result = leegDataframe.to_json(orient="records")
    parsed = loads(result)
    return dumps(parsed, indent=4) 