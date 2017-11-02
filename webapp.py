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
