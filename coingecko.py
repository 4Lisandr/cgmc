import pandas as pd
import requests


def get_content(start, pages=1):
	content = [requests.get(start)]
	for x in range (2, pages+1):
		content.append(requests.get(start +"?page="+str(x)))
	return content

# get_list(get_content(main))
def get_list(req, usd_info=["Price", "Mkt Cap"], change=["1h","24h","7d"], write_csv=False):
	i=1
	allstring = []
	for r in req:
		table = pd.read_html(r.text)[0][["Coin", "Price", "Mkt Cap"]]
		#table = pd.read_html(r.text)[0][["Coin", "Price", "Mkt Cap"]]
		#table = pd.read_html(r.text)[0][["Coin", "Price", "Mkt Cap", "24h","7d"]]
		#table = pd.read_html(r.text)[0][usd_info]

		# todo def refactoring
		table["Coin"] = table ["Coin"].apply(lambda x: x.split("  ")[2])
		for s in usd_info:
			table[s] = table [s].apply(lambda x: x.replace(",","").replace("$",""))
		name ="TopCMC_"+ str(i) +".csv"
		i+=1
		if write_csv:
			table.to_csv(name, index=False)
			print(table)

		allstring.append(table["Coin"])
	return allstring

main = "https://www.coingecko.com/en"
content = get_content(main, 2)
data = get_list(content, write_csv=True)

print(data)
with open("output.txt", "w") as txt_file:
	for line in data:
		txt_file.write("\n".join(line) + "\n")


