import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.in/Smart-AMOLED-Display-Battery-Resistant/dp/B08GXC2NTX/ref=sr_1_5?dchild=1&keywords=band&qid=1613541961&sr=8-5"
response = requests.get(url="https://www.amazon.in/Smart-AMOLED-Display-Battery-Resistant/dp/B08GXC2NTX/ref=sr_1_5?dchild=1&keywords=band&qid=1613541961&sr=8-5"
             ,headers={"Accept-Language": "en-US,en;q=0.9", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"}).text
soup = BeautifulSoup(response, "lxml")
price = soup.find(name="span", id="priceblock_ourprice")
print(price.getText())
actual_price = int(price.getText())


username = "46uday.d@gmail.com"
password = "uday1998"
message = f"The price of the MI Band 5 has come down to Rs 2000. So hurry up and buy it!!!!\nGo to this url-{url}"

if actual_price == 2000 or actual_price < 2000:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(from_addr=username, to_addrs=username, msg=message)
        connection.close()