import pandas as pd
import requests

coingecko = "https://www.coingecko.com/en"
r = requests.get(coingecko)

print(r)