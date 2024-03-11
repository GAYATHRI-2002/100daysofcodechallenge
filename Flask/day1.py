#simple app

from flask import Flask
app = Flask(__name__)

@app.route('/')

def home():
    return "hello gayathri "

if __name__ == '__main__':
    app.run(debug=True)

#app routing
#ststic url
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "This is home page "

@app.route('/about')
def about():
    return "This is about page"


@app.route('/product')
def product():
    return "This is product page"

@app.route('/product/laptop')
def laptop():
    return "This is laptop page"

@app.route('/contact')
def contact():
    return "This is contact page"

app.add_url_rule('/home', 'home', home)



if __name__ == '__main__':
    app.run(debug=True)


#dynamic url

from flask import Flask
app = Flask(__name__)

@app.route('/<int:num1>')
def home(num1):
    return f'{num1}'

@app.route('/<int:age>')
def home(age):
    if age < 18:
        return "Age restriction : not allowed"
    elif age >= 18 :
        return "you aer allowed"
      
@app.route('/about')
def about():
    return "This is about page"


@app.route('/product')
def product():
    return "This is product page"

@app.route('/product/laptop')
def laptop():
    return "This is laptop page"

@app.route('/contact')
def contact():
    return "This is contact page"

app.add_url_rule('/home', 'home', home)



if __name__ == '__main__':
    app.run(debug=True)

#templates

