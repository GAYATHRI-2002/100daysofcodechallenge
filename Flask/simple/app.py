from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')


@app.route('/register', methods=['GET'])
def register():
    name = request.args.get('name')
    number = request.args.get('number')
    email = request.args.get('email')
    return render_template('register.html', name = name, number=number, email=email)


    
@app.route('/about')
def about():
    return render_template('about.html')


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
