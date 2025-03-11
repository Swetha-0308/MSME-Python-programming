from flask import Flask, render_template, request

app=Flask(__name__)
user_login = {}

@app.route('/',methods=['GET','POST'])

def form():
    if request.method=="POST":
        a=request.form.get('user name')
        b=request.form.get('password')
        if (a=="Swetha" and b=="Swe@123"):
            return "login successful"
        else:
            return "Login failed! enter a correct user name and password"

    return render_template('index.html')
if __name__ =='__main__':
    app.run(debug=True)