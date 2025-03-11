from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def application_form():
    # name=''
    # email=''
    # phone=''
    # register_no=''
    # branch=''
    # dob=''
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        register_no = request.form.get('register_no')
        branch = request.form.get('branch')
        dob=request.form.get('dob')
        return render_template('result.html',name=name, email=email, phone=phone, register_no=register_no, branch=branch, dob=dob)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)