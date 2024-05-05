import requests
from bs4 import BeautifulSoup
import lxml
from smtplib import SMTP

AMAZON_URL = "https://www.amazon.ca/SodaStream-Terra-Sparkling-Water-Bundle/dp/B0C2QRCN7Y/?_encoding=UTF8&pd_rd_w=hfH3i&content-id=amzn1.sym.5758671b-686d-4d7c-af22-08ab8e3c615f%3Aamzn1.symc.d10b1e54-47e4-4b2a-b42d-92fe6ebbe579&pf_rd_p=5758671b-686d-4d7c-af22-08ab8e3c615f&pf_rd_r=GD6Y3V71HWP2RMH3V2D1&pd_rd_wg=NeZEf&pd_rd_r=9679f6be-fc4a-4367-a0ce-01ae2e5ffb70&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1"
HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
    "Accept-Language": "en-US,en;q=0.9,en-CA;q=0.8"
}

response = requests.get(url=AMAZON_URL, headers=HEADER)
amazon_webpage = response.text

soup = BeautifulSoup(amazon_webpage, "lxml")
price = float(soup.find(name="span", class_="aok-offscreen").getText().split()[0].replace('$', ''))
print(price)

if price <= 100:
    my_email = "pythonsmtptest282@gmail.com"
    password = "hnzdpcyrkbiyxiyq"
    with SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="jimohadedamola925@gmail.com",
            msg=f"Subject:Amazon Purchase Deal!!! \n\nLow Price Alert!!!!\n\n Price for the Soda Stream Terra Sparkling Water Maker has dropped to ${price}")
        connection.close()
    print(f"Low Price Alert Email Sent.")




