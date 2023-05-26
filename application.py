from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def req(s):
    r = requests.get(s)
def calcam(principal, rate, time, n):

    if principal < 0 or rate < 0 or time < 0:

        return 0
    if n == 1 or n == 2 or n == 4 or n == 12:
        rate = rate / 100
        amount = int(principal * ((1 + (rate / n)) ** (n * time)))
        return amount


    return 0

def calcin(principal, amount):
    if principal < 0:
        amount = 0
        return 0
    interest = int(amount - principal)
    if interest < 0:
        return 0
    return interest

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculate', methods=['POST'])


def calculate():
    principal = float(request.form['principal'])
    rate = float(request.form['rate'])
    time = float(request.form['time'])
    n = float(request.form['n'])

    amount = calcam(principal, rate, time, n)
    interest = calcin(principal, amount)

    return render_template('result.html', amount=amount, interest=interest)

def startsite():
    app.run(debug=True)