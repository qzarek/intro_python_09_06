import requests
import random
import csv


def get_raw_quote(lang="ru"):
    url = "http://api.forismatic.com/api/1.0/"
    key = random.randint(1, 999999)
    params = {"method": "getQuote",
              "format": "json",
              "lang": lang,
              "key": key}
    response = requests.get(url, params=params)
    return response.json()


##### Task 1
def get_quotes(amount):
    quotes = []
    item = 0
    while item < amount:
        quote = get_raw_quote()
        if len(quote['quoteAuthor']) > 0 and quote not in quotes:
            quotes.append(quote)
            item += 1
    return quotes


##### Task 2
def format_quotes_for_csv(quotes):
    formated_quotes = []
    for quote in quotes:
        formated_quotes.append([quote['quoteAuthor'], quote['quoteText'], quote['quoteLink']])
    return formated_quotes


def import_to_csv(formated_quotes):
    data = [['Author', 'Quote', 'URL']]
    data.extend(formated_quotes)
    my_file = open('quotes.csv', 'w')
    with my_file:
        writer = csv.writer(my_file)
        writer.writerows(data)
    return data


# amount = 10
# import_to_csv(format_quotes_for_csv(get_quotes(amount)))

