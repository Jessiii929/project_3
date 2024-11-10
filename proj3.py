from flask import Flask, jsonify, render_template
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import and_
import datetime as dt


app = Flask(__name__)

@app.route("/")
def prop1():
    
    return render_template('homepage.html')


@app.route("/map1") 
def prop2(): 
    return render_template('index.html')

@app.route("/map_year")
def prop3():
    return render_template('safest_cities.html')

@app.route("/crime_heatmap")
def prop4():
    return render_template('crime_heatmap.html')

@app.route("/data")
def prop5():
    return render_template('data.html')

@app.route("/crime_map_2014")
def prop6():
    return render_template('crime_map_2014.html')

@app.route("/viz")
def prop7():
    return render_template('visualizations.html')


if __name__ == "__main__":
    app.run(debug=True)
