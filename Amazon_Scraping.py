import requests
from bs4 import BeautifulSoup
import smtplib


URL='https://www.amazon.in/boAt-BassHeads-100-Headphones-Black/dp/B071Z8M4KX/ref=lp_22120007031_1_1?s=electronics&ie=UTF8&qid=1598556455&sr=1-1'

headers={"your User agent//type my user agent in chrome and copy paste the URL appearing in the first "}

def check_price():
    page = requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')

    title= soup.find(id="productTitle").get_text()
    price=soup.find(id="priceblock_ourprice").get_text()
    converted_price=float(price[1:3])
     
    if(converted_price < 200.0):
        send_mail()
    
    
    print(converted_price)
    print(title.strip())


def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('your Gmail id','your app password')

    subject='Price Fell Down'
    body='check the amazon link https://www.amazon.in/boAt-BassHeads-100-Headphones-Black/dp/B071Z8M4KX/ref=lp_22120007031_1_1?s=electronics&ie=UTF8&qid=1598556455&sr=1-1'
    msg=f"Subject:{subject}\n\n{body}"
    server.sendmail(
        'To',
        'From',
        msg
    )
    
    print("Hey Mail has been sent")
    server.quit()


check_price()
