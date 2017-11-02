from flask import Flask, url_for, render_template, request, Markup, flash
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)

def get_state_options():
    state = counties[0]["State"]
    choice = ""
    for c in counties:
        if state != c["State"]:
            choice += Markup("<option value=" + state +">" + state + "</option>")
            state = c["State"]
    return choice

def get_statefact(state):
    funfact = ""
    for c in counties:
        if state == c["State"]:
            fact = c["Age"]["Percent Under 18 Year"]
            statefact += Markup("<p>" + str(fact) + "</p>")
    return statefact

@app.route("/")
def render_main():
   return render_template('index.html', option = get_state_options())

@app.route("/", methods=['POST'])
def render_fact():
    place = request.args['data']
    render_template('index.html', fact = get_statefact(place))
