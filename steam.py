#!/us/bin/python
import json
import requests
import string
import re

page = requests.get("https://steamcommunity.com/market/listings/753/480490-DR%20IGWE")

parsed = page.text.splitlines()

for line in parsed:
    lparsed = line.strip()
    m = re.search('^Market_LoadOrderSpread\((.+?)\)', lparsed)
    mm = re.search('\"market_listing_item_name\" style=\"\">(.+?)</span><br/>', lparsed)

    if m:
        item_id = m.group(1).strip()
    if mm:
        item_name = mm.group(1).strip()


if item_id != "" and item_name != "":
    print("card found!")

    quote_page = requests.get('https://steamcommunity.com/market/itemordershistogram?country=ES&language=english&currency=3&item_nameid='+item_id+'&two_factor=0')

    name_box = json.loads(quote_page.text)
    price = name_box['sell_order_graph'][0][0]
    print("card >>> " + item_name + " id: " + item_id + " price: " + str(price))