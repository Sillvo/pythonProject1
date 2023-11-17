currency = dict()
currency["USD"]=0.0107276
currency["EUR"]=0.0101677268
currency["UZS"]=130.98503365
for key, value in currency.items():
    print(f"{key}: {value}")
print('Query format: ' + "100 USD>RUB")
your_query=input("Input your query: ").split()
currency_count=round(float(your_query[0]),2)
currency_first=str(your_query[1][:3])
currency_second=str(your_query[1][-3:])
if currency_first == "RUB":
    result = round((currency.get(currency_second)) * currency_count, 2)
elif currency_first != "RUB" and currency_second == "RUB":
    result = round(currency_count / (currency.get(currency_first)), 2)
elif currency_first != "RUB" and currency_second != "RUB":
    result = round(currency_count / (currency.get(currency_first)) * currency[currency_second], 2)
else:
    result = (currency.get(currency_first)) * 10000 * currency_count
formated_result= "{:,}".format(result).replace(',',' ')
print("Result: "+str(currency_count)+" "+currency_first+" = "+ formated_result+" "+currency_second)