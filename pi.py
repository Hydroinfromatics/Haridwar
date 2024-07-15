from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dadpur')
def dadpur():
    return redirect("https://dadpur.onrender.com/dashboard/")

@app.route('/suman-nagar')
def suman_nagar():
    return redirect("https://suman-nagar.onrender.com/dashboard/")

if __name__ == '__main__':
    app.run(debug=True)