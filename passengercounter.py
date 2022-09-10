from replit import db
from Flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
return 'layout.html'

@app.route('/increment')
def increment
db['number']+=1
return render_template('passanger.layout.html', number=db['number'])

@app.route('/decrement')
def decrement
db['number']-=1
return render_template('passanger.layout.html', number=db['number'])







app.run(host='0.0.0.0', port=81)