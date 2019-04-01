from myproject import app # importa o app da linha 7 do __init__.py
from flask import render_template

@app.route('/')
def index():
	return render_template('home.html')

if __name__ == '__main__':
	app.run(debug = True)