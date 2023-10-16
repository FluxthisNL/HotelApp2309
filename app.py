from flask import Flask
from flask_cors import CORS, cross_origin
import felixprobeersels
import filterMarktenOpArtikelen
import jeroenprobeer
import zaidtest
import searchRestaurants
import infoPerBestand
from flask import render_template, jsonify, request

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def helloWorld():
    return "Hello, Fijne dag!"

@app.route("/felix/<eengegeven>")
@cross_origin()
def methodefelix(eengegeven):
    return felixprobeersels.functiefelix(eengegeven)

@app.route("/markten/<artikelen>")
@cross_origin()
def filterMarkten(artikelen):
    return filterMarktenOpArtikelen.filter(artikelen)

@app.route("/marktenkaart")
@cross_origin()
def marktKaart():
    return render_template('markten_kaart.html')

@app.route("/alleinfo/<bestandsnaam>")
@cross_origin()
def methodeAlleInfo(bestandsnaam):
    return infoPerBestand.alleInfo(bestandsnaam)

@app.route("/jeroen/<mijngegeven>")
@cross_origin()
def methodejeroen(mijngegeven):
    return jeroenprobeer.jeroenfunctie(mijngegeven)

@app.route("/jeroen2/<invoer>")
@cross_origin()
def methodejeroen2(invoer):
    return searchRestaurants.search_csv_for_keywords(invoer)

@app.route("/jeroen3/<mijngegeven>")
@cross_origin()
def methodejeroen3(mijngegeven):
    return searchRestaurants.filter_and_dropdown(mijngegeven)

@app.route("/jeroen4/")
@cross_origin()
def methodejeroen4():
    result = searchRestaurants.restaurantNumbers(rating_treshold=4.0)
    return result

@app.route("/Zaid2")
@cross_origin()
def functiemaakmap():
    return zaidtest.functiezaid2()

@app.route("/Zaid3/<mijngegeven>")
@cross_origin()
def functiezaid3zoek(mijngegeven):
    return zaidtest.functiezaid3zoek(mijngegeven)

@app.route("/Zaid4/<mijngegeven>")
@cross_origin()
def functiemap(mijngegeven):
    return zaidtest.functiezaid4index(mijngegeven)

@app.route("/Zaid5/<mijngegeven>")
@cross_origin()
def fuctiepointerinfo(mijngegeven):
    return zaidtest.functiezaid4index(mijngegeven)

@app.route("/ZoekLocatieMusea/<invoer>")
@cross_origin()
def zoek_locatie_in_CSV(invoer):
    return zaidtest.functie_zoek_locatie_in_CSV(invoer)
