import pandas as pd
import requests

exchanges=["binance", "uniswap_v2"]
ex = exchanges[0]
page = "https://www.coingecko.com/en/exchanges/"+ex
r = requests.get(page)
fields = ["Coin", "Pair","Price","24h Volume","Volume %"]
table = pd.read_html(r.text)[0][fields]

print(table)

name = ex+"_.csv"
table.to_csv(name, index=False)