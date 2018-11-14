# Python & Flask
A repository to practice creating a website using Python and Flask.

## Important Terms
1. *Framework*


## Introduction: Flask Tutorial
**How do you take any Python function, and create a web interface for it?**

First, I will be following the tutorial on [Arya Boudaie's Personal Site](https://aryaboudaie.com/python/technical/educational/web/flask/2018/10/17/flask.html?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more)

### Hello, World
'@app.route('/test')'
> This specifies the route for a function. When this path is visited by the localhost, then the function it is attached to is called.

### Taking input, string
'@app.route('/test/<name>')'
> This is a way to store part of the name of the url, which can be accessed for the function this app is attached to.

### Taking input, int 
'@app.route('test/<int:num>')'
> This is a way to store an int from the url.

## Creating Aesthetic Pages
*HTML will enable you to create nice-looking pages*

### HTML String
'html = "< h1 > The square of " + num + " is " + num ** 2'
> You can write in HTML to present information on the screen more elegantly.

### Junja2
> Jinja is a an example of an HTML templating engine that can help develop HTML efficiently.

## Keeping track of state

### Session
> Import session that is a dictionary associated with each site user. Session stores data on a given user and persists.