import requests
import sys
import json

try:
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    else:
        sys.argv[1] = float(sys.argv[1])

except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")


object = response.json()
print(json.dumps(response.json(), indent=2))

rate = object["bpi"]["USD"]["rate_float"]
print(rate)

num = sys.argv[1]

amount = num * rate

print(f"${amount:,.4f}")
