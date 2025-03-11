from flask import Flask, render_template, request

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])

def menu():

    if request.method=='POST':
        dosa=request.form.get("dosa")
        idly=request.form.get("idly")
        pongal=request.form.get("pongal")
        vada=request.form.get("vada")
        poori=request.form.get("poori")
        tea=request.form.get("tea")
        coffee=request.form.get("coffee")
        milk=request.form.get("milk")
        upma=request.form.get("upma")
        apple_juice=request.form.get("apple_juice")
        butter_milk=request.form.get("butter_milk")
        butter_biscuit=request.form.get("butter_biscuit")
        sandwich=request.form.get("sandwich")



    return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True)
