import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL="https://www.amazon.in/dp/B07DJHXTLJ?pf_rd_p=fa25496c-7d42-4f20-a958-cce32020b23e&pf_rd_r=0Z0RJJKCESSD1ZX1R1BA"

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36' }


def check_price():
    page = requests.get(URL, headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    title=soup.find(id="productTitle").get_text()
    price= soup.find(id="priceblock_dealprice").get_text()
    print(title.strip())
    convertedprice=price[2:]
    print(convertedprice)


    wantprice="36,000.00"
    if(convertedprice<wantprice):
        send_mail()

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('sidmehta0201@gmail.com','qehkgdqfrtkyjote')

    subject='Prce Fall Down!!!'
    body="Check the amazon link  "+URL

    msg=f"Subject:{subject}\n\n{body}"

    server.sendmail('sidmehta0201@gmail.com','sidmehtavines@gmail.com',msg)

    print("Hey Email has been Sent!!!!")

    server.quit()

while(True):
    check_price()
    time.sleep(60)