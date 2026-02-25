stock=[
{"name":"hot dog combo", "price": 1.50, "desc": "a hot dog and a drink"}
,
{"name":"80in TV","price":999.99,"desc":"a 4K UHD 80in Samsung TV"}
,
{"name":"LEGO Nissan Skyline","price":72.95,"desc":"Miniature Nissan Skyline made out of LEGO"}
]
for index, item in enumerate(stock):
    print(index, ":", item["name"])
item=int(input("Please enter the index number of the item of want to purchase: "))
print(stock[item]["name"])