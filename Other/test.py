import sys

currency = {}
for i in open("currencies.txt"):
    code, value = i.strip().split()
    currency[code] = (float(value))
j = 0
for key, value in currency.items():
    if j == 3:
        print(f"{key}: {value: 9.4f}", end="  |  \n")
        j = 0
    else:
        print(f"{key}: {value: 9.4f}", end="  |  ")
        j = j + 1
print('\n')
while True:
    print('Query format: 100 USD>RUB')
    s = input("Input your query: ")
    # Разбиваем строку по пробелам на составляющие для дальнейшего использования
    your_query = s.split()
    if s == "0" or s == '':
        # Проверяем что не введено 0 или пустая строка, если да, то завершаем работу
        sys.exit()
    # Количество валюты
    currency_count = float(your_query[0])
    # Из какой валюты перевести
    currency_first = str.upper(your_query[1][:3])
    # В какую валюту перевести
    currency_second = str.upper(your_query[1][-3:])
    if currency_first == "RUB":
        # Если нужно перевести рубли, то умножаем курс желаемой валюты в к рублу на количество
        result = round((currency.get(currency_second)) * currency_count, 2)
    elif currency_second == "RUB":
        # Перевод в рубли. Количество валюты делим на курс
        result = round(currency_count / (currency.get(currency_first)), 2)
    else:
        # Валюта в валюту. Количество делим на курс первой и умножаем на курс второй
        result = round(currency_count / currency[currency_first] * currency[currency_second], 2)
    format_result: str = "{:,}".format(result).replace(',', ' ')
    # Разбиваем на разряды то что получилось
    print(
        "Result: " + str(currency_count) + " " + currency_first + " = " + format_result + " " + currency_second + "\n")
