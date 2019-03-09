from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    fruits = {
    'straw': str(request.form.get('strawberry')),
    'rasp': str(request.form.get('raspberry')),
    'apple': str(request.form.get('apple')),
    'black': str(request.form.get('blackberry')),
    }
    num = int(fruits['straw']) + int(fruits['rasp']) + int(fruits['apple']) + int(fruits['black'])
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%B")
    day = now.strftime("%-d")
    time = now.strftime("%I:%M:%S %p")
    date = ' '.join([day, month, year, 'at', time])
    order = f'We ordered {num} items for you and charged your student account on {date}.'
    fname = request.form['first_name']
    lname = request.form['last_name']
    student_id = request.form['student_id']

    print(f'Charging {fname} {lname} for {num} items of fruit')
    return render_template("checkout.html", order=order, fruits=fruits, fname=fname, lname=lname, student_id=student_id)

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)
