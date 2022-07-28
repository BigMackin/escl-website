from flask import Flask, url_for
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about/')
def about():
    return render_template('about.html')
    
@app.route('/schedule/')
def schedule():
    return render_template('schedule.html')

@app.route('/stats/')
def stats():
    return render_template('stats.html')

if __name__=='__main__':
    app.run(debug=True)