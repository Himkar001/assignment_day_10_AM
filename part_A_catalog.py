from collections import defaultdict

catalog = {
"SKU001": {"name":"Laptop","price":65000,"category":"electronics","stock":15,"rating":4.5,"tags":["computer","work"]},
"SKU002": {"name":"Phone","price":30000,"category":"electronics","stock":10,"rating":4.4,"tags":["mobile"]},
"SKU003": {"name":"Headphones","price":2000,"category":"electronics","stock":0,"rating":4.2,"tags":["music"]},

"SKU004": {"name":"Tshirt","price":700,"category":"clothing","stock":25,"rating":3.9,"tags":["fashion"]},
"SKU005": {"name":"Jeans","price":1500,"category":"clothing","stock":5,"rating":4.1,"tags":["fashion"]},
"SKU006": {"name":"Jacket","price":3000,"category":"clothing","stock":0,"rating":4.3,"tags":["winter"]},

"SKU007": {"name":"Python Book","price":800,"category":"books","stock":20,"rating":4.7,"tags":["education"]},
"SKU008": {"name":"DS Book","price":900,"category":"books","stock":12,"rating":4.6,"tags":["data"]},
"SKU009": {"name":"Novel","price":400,"category":"books","stock":0,"rating":3.8,"tags":["story"]},

"SKU010": {"name":"Chocolate","price":200,"category":"food","stock":50,"rating":4.5,"tags":["sweet"]},
"SKU011": {"name":"Cookies","price":150,"category":"food","stock":35,"rating":4.0,"tags":["snack"]},
"SKU012": {"name":"Chips","price":100,"category":"food","stock":0,"rating":3.9,"tags":["snack"]},

"SKU013": {"name":"Monitor","price":12000,"category":"electronics","stock":7,"rating":4.3,"tags":["computer"]},
"SKU014": {"name":"Sneakers","price":2500,"category":"clothing","stock":8,"rating":4.2,"tags":["sports"]},
"SKU015": {"name":"Cookbook","price":600,"category":"books","stock":14,"rating":4.4,"tags":["recipe"]}
}

def search_by_tag(tag):
    result = defaultdict(list)

    for sku,product in catalog.items():
        for t in product.get("tags",[]):
            result[t].append(product.get("name"))

    return result.get(tag,[])

def out_of_stock():
    return {sku:prod for sku,prod in catalog.items() if prod.get("stock")==0}

def price_range(min_price,max_price):
    return {sku:prod for sku,prod in catalog.items() if min_price<=prod.get("price")<=max_price}

def category_summary():

    data = defaultdict(list)

    for product in catalog.values():
        data[product.get("category")].append(product)

    summary = {}

    for cat,items in data.items():

        count=len(items)
        avg_price=sum(i.get("price") for i in items)/count
        avg_rating=sum(i.get("rating") for i in items)/count

        summary[cat]={
        "count":count,
        "avg_price":avg_price,
        "avg_rating":avg_rating
        }

    return summary


print(search_by_tag("fashion"))
print(out_of_stock())
print(price_range(500,2000))
print(category_summary())