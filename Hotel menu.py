menu={
    "idly":10,
    "dosa":15,
    "puri":12,
    "tea":15,
    "milk":12,
    "butter biscuit":5,
    "coffee":20,
    "pongal":25,
    "vada": 8,
    "upma":10
}
order = {}
for key, value in menu.items():
    print(f'{key:15} ${value}')
price = 0

while True:
    food=input("Enter your order (press q for exit): ")
    if food == "q":
        for key, value in order.items():
            print(f'{key:15} {value}')
        print(f"Total Price = ${price}")
        print("THANK YOU VISIT AGAIN !!!")
        break

    elif food not in menu:
        print(f'{food} is not in menu')
    else:
        while(True):
            count=input("Enter quantity: ")

            if not count.isdigit() or int(count) <= 0:
                print("Enter a valid number")
                continue
            else:
                price += int(count) * menu[food]
                order[food] = [f'{count} X $ {menu[food]} = $ {int(count) * menu[food]}']
                break