#!/usr/bin/python3

import requests

def main():
    quote = requests.get("https://quotes.rest/qod?language=en")
    quote= quote.json()
    print(quote)
 #   print(f"Today's quote is from {quote[][][][]}:")
#    print(f'{quote[][][][]}')

main()
