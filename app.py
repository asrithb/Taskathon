from flask import Flask, send_from_directory
import os
from taipy.gui import Gui
import taipy.gui.builder as tgb

app = Flask(__name__)

# Directory where your HTML and assets are stored
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

# Serve assets like CSS, JS, and images
@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('assets', path)

# Taipy GUI setup
league_name = tgb.state(default="")

with tgb.Page() as page:
    tgb.input(league_name, label="Enter League Name")
    tgb.button("Submit", on_click=lambda: print(f"League Name: {league_name()}"))

# Initialize the Taipy GUI on a different endpoint
Gui(page=page).run(port=5001, path="/taipy")

if __name__ == "__main__":
    app.run(debug=True, port=5000)



