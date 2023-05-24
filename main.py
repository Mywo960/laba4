from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    principal = float(request.form['principal'])
    rate = float(request.form['rate']) / 100
    time = float(request.form['time'])
    n = float(request.form['n'])

    amount = int(principal * ((1 + (rate/n)) ** (n*time)))
    interest = int(amount - principal)

    return render_template('result.html', amount=amount, interest=interest)

if __name__ == '__main__':
    app.run(debug=True)