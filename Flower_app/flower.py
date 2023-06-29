from flask import Flask,  render_template, request, redirect


app= Flask(__name__)
app.secret_key='secret key'

@app.route('/')
def home():
    return render_template('flowerindex.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/about')
def about():
    return render_template('aboutflower.html')

@app.route('/contact')
def contact():
    return render_template('contactflower.html')

if __name__=='__main__':
    app.run(debug=True)
