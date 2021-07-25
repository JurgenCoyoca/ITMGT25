products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

# Problem 1
def get_product(code):
    return products[code]

# Problem 2
def get_property(code,property):
    return products[code][property]

# Problem 3
def main():
    productsorter = []
    tempreceiptlist = []
    sortedreceiptlist = []
    session = True

    while(session==True):
        order_input = input('Input product code and quantity here (product code,quantity):')
        order = order_input.split(',')
        if order_input == "/":
            session = False

        else:
            product_code = order[0]
            quantity = int(order[1])

            if (product_code in productsorter) == False:
                productsorter.append(product_code)
                productdict = {"product_code":product_code,"quantity":quantity}
                tempreceiptlist.append(productdict)
                productdict = {}
            elif (product_code in productsorter) == True:
                for i in range(len(productsorter)):
                    if tempreceiptlist[i]["product_code"] == product_code:
                        tempreceiptlist[i]["quantity"] += quantity
                        break

    productsorter.sort()
    for i in range(len(productsorter)):
        for j in range(len(productsorter)):
            if productsorter[i] == tempreceiptlist[j]["product_code"]:
                sortedreceiptlist.append(tempreceiptlist[j])
                break

    quantity = 0
    total = 0
    receipt = '==\nCODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL\n'
    for i in range(len(sortedreceiptlist)):
        code = sortedreceiptlist[i]["product_code"]
        name = get_product(sortedreceiptlist[i]["product_code"])["name"]
        quantity = sortedreceiptlist[i]["quantity"]
        subtotal = quantity*get_property(sortedreceiptlist[i]["product_code"],"price")
        total += subtotal
        receipt += (f"{code}\t\t\t{name}\t\t\t{quantity}\t\t\t{subtotal}\n")
    receipt += (f"\nTotal:\t\t\t\t\t\t\t\t\t\t{total}\n==")

    with open("receipt.txt","w") as r:
        r.write(receipt)

main()
