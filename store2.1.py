stock=[
{"name":"hot dog combo", "price": 1.50, "desc": "a hot dog and a drink"}
,
{"name":"80in TV","price":999.99,"desc":"a 4K UHD 80in Samsung TV"}
,
{"name":"LEGO Nissan Skyline","price":72.95,"desc":"Miniature Nissan Skyline made out of LEGO"}
]   #items in stock
for index, item in enumerate(stock):
    print(index, ":", item["name"]) #prints list of items & their index inside stock
cart=[]  #list of items you buy
item=int(input("Please enter the index number of the item of want to purchase: "))  #asks the items from stock you want
cart.append(stock[item])    #adds the item you input into cart
cashier=input("Are you done shopping yet? yes/no ")  #asks if you are done shopping
register=cashier.lower()    #makes the answer for cashier lowercase
while register=="no":
    item=int(input("Please enter the index number of the item of want to purchase: "))  #as long as register says no, you will be asked to input another item from stock
if register=="yes":
    for index, item in enumerate(cart):
        print(index, ":", item["name"])
else:
    cashier=input("Are you done shopping yet? yes/no")