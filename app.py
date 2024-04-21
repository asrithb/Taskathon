from flask import Flask, send_from_directory
import os
from taipy import State
from taipy.gui import Gui
import taipy.gui.builder as tgb

app = Flask(__name__)

# Define the state variable
league_name = State(default="")

# Taipy GUI setup
with tgb.Page() as page:
    tgb.input(league_name, label="Enter League Name")
    tgb.button("Submit", on_click=lambda: print(f"League Name: {league_name.get()}"))

# Initialize the Taipy GUI on a different endpoint
Gui(page=page).run(port=5001, path="/taipy")

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('assets', path)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
