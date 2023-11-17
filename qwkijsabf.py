import sys

while True:
    print('Query format: 100 USD>RUB')
    s = input("Input your query: ")
    if not s or s == "0":
        sys.exit()
    currency_count, currency_pair = s.split()
    currency_count = float(currency_count)
    currency_first, currency_second = currency_pair[:3].upper(), currency_pair[-3:].upper()
    if currency_first == "RUB":
        result = round((currency.get(currency_second))*currency_count, 2)
    elif currency_first != "RUB" and currency_second == "RUB":
        result = round(currency_count/(currency.get(currency_first)), 2)
    elif currency_first != "RUB" and currency_second != "RUB":
        result = round(currency_count/(currency.get(currency_first))*currency[currency_second], 2)
    else:
        result = (currency.get(currency_first))*10000*currency_count
    formated_result = "{:,}".format(result).replace(',', ' ')
    print(f"Result: {currency_count} {currency_first} = {formated_result} {currency_second}n")