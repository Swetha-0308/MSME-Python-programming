from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operator = request.form['operator']

        if operator == 'add':
            result = num1 + num2
        elif operator == 'subtraction':
            result = num1 - num2
        elif operator == 'multiplication':
            result = num1 * num2
        elif operator == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                return 'Error! Division by zero is not allowed.'
        else:
            return 'Invalid operator.'

        return render_template('index.html', result=result)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)