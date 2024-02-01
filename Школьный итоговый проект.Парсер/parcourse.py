import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'http://www.cbr.ru/scripts/XML_daily.asp?'

today = datetime.today()
today = today.strftime('%d/%m/%Y')
now = datetime.now()
day = ("{}.{}.{}".format(now.day, now.month, now.year))
time = ("{}:{}".format(now.hour,now.minute))
print(today)
payload = {'date_req' : today}



responce = requests.get(url, params=payload)

xml = BeautifulSoup(responce.content, 'lxml')


def getCourse(id):
    return xml.find('valute', {'id' : id}).value.text

print(getCourse('R01215'),'рублей за 1 Датскую крону')
print(getCourse('R01700J'),'рублей за 1 Турецкую лиру')
print(getCourse('R01805F'),'рублей за 1 Сербский динар')
print(getCourse('R01820'),'рублей за 1 Японский иен')
print(getCourse('R01235'), 'рублей за 1 доллар')
print(getCourse('R01239'), 'рублей за 1 евро')
print(getCourse('R01375'), 'рублей за 1 юань')

print(responce.url)












