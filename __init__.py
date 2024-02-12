from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)  

@app.route("/contact/")
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"

@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")

@app.route("/paris/")
def meteo():
    response = urlopen('https://developers-dot-devsite-v2-prod.appspot.com/chart/interactive/docs/gallery?hl=fr')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15 # Conversion de Kelvin en °c 
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)

                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html') #Comm11
  
if __name__ == "__main__":
  app.run(debug=True)
