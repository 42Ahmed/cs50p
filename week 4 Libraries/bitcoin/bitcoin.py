import requests
import sys
import json

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    number = float(sys.argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    price = o["bpi"]["USD"]["rate_float"]
    total = number * price
    print(f"${total:,.4f}")

except requests.RequestException:
    sys.exit()
except:
    sys.exit("Command-line argument is not a number")