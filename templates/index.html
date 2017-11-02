from flask import Flask, url_for, render_template, request, Markup, flash
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

def get_state_options():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    state = counties[0]["State"]
    choice = ""
    for c in counties:
        choice += Markup("<option value=" + state +">" + state + "</option>")
        state = c["State"]
    return choice

@app.route("/")
def render_main():
    get_state_options()
    return render_template('home.html', option = get_state_options())
    
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
