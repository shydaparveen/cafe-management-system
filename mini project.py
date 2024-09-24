#  dictionary with conditional
menu={"passta":230,"pizza":80, "burger":100, "coffe":70,"salad":60}
print("Welcome to Python Restaurant")
print(" passta :230\n pizza:80\n burger:100\n coffe:70\n salad:60")
order_total=0
item_1=input("enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item (item1)has been order to your order")
else:
    print(f"order item {item_1} is not available yet!")
another_order= input("do you want to another order?(yes/no)")
if another_order =="yes":
    item_2= input("enter the name of seconf item ==")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added")
    else:
        print(f"order item {item_2} is not available yet!")
print(f"The total amount of item is {order_total}")
