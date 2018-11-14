from flask import Flask, render_template, session

app = Flask(__name__)

app.secret_key = 'test123'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
def landingPage():
	x = session.get('x', None) 
	if not x:
		session['x'] = 1
	elif x>=10:
		session.clear()
		return "Session Cleared"
	else:
		session['x']+=1
	return "Number of refreshes: "+str(session['x'])

@app.route('/test') 
def helloWorld():
	return 'Hi! Please type in /name into your URL.'

@app.route('/test/<name>')
def askName(name):
	return 'Hello, ' + name + '!'

def factors(num):
  return [x for x in range(1, num+1) if num%x==0]

def squareNum(num):
	return "<h1> The square of " + str(num) + " is " + str(num ** 2)

@app.route('/test/<int:num>')
def formattedFactors(num):
	return render_template(
		"factors.html",  			# name of template
		number = num,  				# value for `number` in template
		factors = factors(num) 		# value for `factors` in template
	)

if __name__ == '__main__':
	app.run(host = '0.0.0.0')