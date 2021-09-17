import pandas as pd
import requests

coingecko = "https://www.coingecko.com/en"
r = requests.get(coingecko)
fields = ["Coin", "Price", "Mkt Cap", "1h","24h","7d"]
table = pd.read_html(r.text)[0][fields]

#left symbol only
table["Coin"] = table ["Coin"].apply(lambda x: x.split("  ")[2])
for s in fields[1], fields[2]:
	table[s] = table [s].apply(lambda x: x.replace(",","").replace("$",""))

print(table)