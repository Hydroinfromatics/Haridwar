from flask import Flask, render_template, redirect
import os

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
    # Use PORT environment variable if available, otherwise default to 8080
    port = int(os.environ.get('PORT', 8080))
    
    # Run the app
    app.run(host='0.0.0.0', port=port, debug=True)
