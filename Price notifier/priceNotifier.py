from bs4 import BeautifulSoup
import requests
import smtplib
re=requests.get("http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html")
contents=re.content
soup=BeautifulSoup(contents,"html.parser")
price=float(soup.find("p","price_color").text[1:])

if(price<60):
    smt=smtplib.SMTP("smtp.gmail.com",587)
    smt.ehlo()
    smt.starttls()
    smt.login('nuysanbarorodev@gmail.com',"cdctafycvxbsodmy")
    smt.sendmail("nuysanbarorodev@gmail",
        "nuysanbarorodev@gmail.com",
        f"Subject:Headphones price notifier \n\n the price of the book has dropped to {price} go buy it")
    smt.quit()