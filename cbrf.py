import requests
from xml2dictionary import xml2dictionary
url = 'https://cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To='
url += input("Введите дату в формате ДД.ММ.ГГГГ")
