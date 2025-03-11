from flask import Flask, render_template, request

app = Flask(__name__)

# Define the menu
menu = {
    "dish1": {"name": "dosa", "price": 15},
    "dish2": {"name": "idly", "price": 10},
    "dish3": {"name": "pongal", "price": 25},
    "dish4": {"name": "poori", "price": 15},
    "dish5": {"name": "vada", "price": 5},
    "dish6": {"name": "coffee", "price": 15},
    "dish7": {"name": "tea", "price": 12},
    "dish8": {"name": "milk", "price": 10},
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_dishes = request.form.getlist('dish')
        quantities = request.form.getlist('quantity')

        total_bill = 0
        bill_details = []
        for i in range(len(selected_dishes)):
            dish_id = selected_dishes[i]
            quantity = int(quantities[i])
            dish_name = menu[dish_id]['name']
            price = menu[dish_id]['price']
            total_price = price * quantity
            total_bill += total_price
            bill_details.append({"dish": dish_name, "quantity": quantity, "price": price, "total_price": total_price})

        return render_template('bill.html', bill_details=bill_details, total_bill=total_bill)

    return render_template('index1.html', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)