from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'this is a secret key for the dojo survey assignment'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    session['user_name'] = request.form['name']
    session['user_location'] = request.form['location']
    session['user_language'] = request.form['language']
    session['user_comments'] = request.form['comments']
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')

if __name__=='__main__':
    app.run(debug=True)