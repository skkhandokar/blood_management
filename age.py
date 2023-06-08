

# from datetime import datetime,date

# my_date = input("Enter B'date in mmm/dd/yyyy format:")


# b_date = datetime.strptime(my_date, '%d/%m/%Y')
# age=int((datetime.today() - b_date).days/365)


# myday=int(my_date[:2])
# today=int(date.today().strftime("%d"))

# mymonthmonth=int(my_date[3:5])
# todaymonth=int(date.today().strftime("%m"))

# print (age)
# print(abs (todaymonth-mymonthmonth))
# print(abs (today-myday))

print("Standard Express")

print("Standard Express,Standard Express - Collection Point,Standard Express - Pick Locker")

print("Standard Express")
import requests
from bs4 import BeautifulSoup 
url = 'https://www.example.com' 
response = requests.get(url) 
soup = BeautifulSoup(response.text, 'html.parser') 
print(soup.prettify())


import requests
from bs4 import BeautifulSoup

url = 'https://shopee.sg/GS-GA100-Black-Gold-Men%27s-Fashion-Sports-Quartz-Watch-GA-100-LED-Automatic-Luminous-Waterproof-Watch-i.829923962.19743739633?sp_atk%3D183a4a2b-ff4e-46c0-8e81-9006bab65384%26xptdk%3D183a4a2b-ff4e-46c0-8e81-9006bab65384'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Extract the title of the page
color_tag = soup.find("color")
if color_tag:
    title = color_tag.string
else:
    title = None

# Extract the price of the product
price_tag = soup.find('div', {'class': '_3n5NQx'})
if price_tag:
    price = price_tag.text
else:
    price = None

print('Title:', title)
print('Price:', price) 