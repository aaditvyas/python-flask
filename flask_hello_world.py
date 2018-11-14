from flask import Flask

""" Create the App
- Creating a new "app" which will be run.
- The app will be used to manage the things the website will be able to do.
"""
app = Flask(__name__)

# decorator: This is the line on top of a function that turns it into a "route"
@app.route('/') # this is the default route, when nothing else if given to the url
def helloWorld(): # what does the url return
	return 'Hello World!'

@app.route('/test')
def routeTest():
	return 'This is testing the /test route'

# run the app
if __name__ == '__main__': # python: run this code only if I run it
	app.run(host = '0.0.0.0') # runs the app created above and makes it run on a localhost