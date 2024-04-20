class Task:
    def __init__(self, name, points, passed):
        self.name = name
        self.points = points
        self.passed = passed
        

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(debug=True)



