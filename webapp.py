
from flask import Flask, url_for, render_template, request, markups

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

def get_state_options():
    op = Markup("<option value="memes">" + "memes" + "</option>")
    return op

@app.route("/")
def render_main():
    get_state_options()
    return render_template('home.html', option = get_state_options())
    
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
