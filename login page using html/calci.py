from flask import Flask, render_template, request

calci = Flask(__name__)

@calci.route("/", methods = ['GET', 'POST'])
def add_numbers():
    if request.method == 'POST':
        a = request.form.get("number_1")
        b = request.form.get("number_2")
        c = request.form.get("operator")
        if c == '+':
            return f'The sum of {a} and {b} is {int(a)+int(b)}'
        elif c == '-':
            return f'When {a} is subtracted by {b} its {int(a)-int(b)}'
        elif c == "*":
            return f"When {a} is multiplied by {b} its {int(a)*int(b)}"
        elif c == "/":
            return f'When {a} is divided by {b} its {int(a)/int(b)}'
    return render_template('index1.html')

if __name__ == '__main__':
    calci.run(debug=True)