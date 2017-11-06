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
    fact = 0
    numCounties = 0
    for c in counties:
        if state == c["State"]:
            fact += c["Age"]["Percent Under 18 Years"]
            numCounties += 1
    fact = round(fact/numCounties,2)
    funfact = Markup("<p>" + "Percent of People Under the age of 18 Years in " + state + " is, " + str(fact) + "%" + "</p>")
    return funfact

@app.route("/")
def render_main():
   return render_template('index.html', option = get_state_options())

@app.route("/app", methods=['GET','POST'])
def render_fact():
    area = request.args['dat']
    return render_template('index.html', fact = get_statefact(area), option = get_state_options())

if __name__=="__main__":
     app.run(debug=False, port=54321)
