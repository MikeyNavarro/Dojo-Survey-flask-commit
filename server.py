import re
from flask import Flask, render_template, request, redirect , session
app = Flask(__name__)
app.secret_key = "im kool"

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/submit' , methods=['POST'])
def submit():
  print(request.form)
  session["name"] = request.form["name"]
  session['DojoLocation'] = request.form['DojoLocation']
  session['language'] = request.form['language']
  session['comment'] = request.form['comment']
  return redirect('/result')

@app.route('/result')
def result():
  return render_template('result.html')

if __name__ == '__main__':
  app.run(debug=True)
