
import yagmail
import requests
from bs4 import BeautifulSoup
import time
import random
from hidden import bot_email, bot_key, mail_to


def send_email(bot_email, bot_key, mail_to):

    subject = "Automated GFX Bot message"
    content = "New IN STOCK item(s) reported! Email comfirmation is now turned off."
    yagmail.SMTP({bot_email: "GFX Bot"}, bot_key).send(mail_to, subject, content)


url = "https://www.newegg.com/Video-Card/EventSaleStore/ID-1173"  # Any event sale store - debug: out of stock
# url = "https://www.newegg.com/p/pl?d=AMD+Radeon+RX+6900+XT"  # Any newegg seach request - debug: in stock
# url = "https://www.newegg.com/p/pl?d=3090+ti&N=100006662%208000"  # Mix in/out
connections_made = 0
instock_found = 0
send_email_confirmation = False
cool_list = []

while True:

    ## Long delay between connections to be safe
    random_wait_time = random.randrange(520, 1200)
    print("")
    print(f"--- Current wait time: {random_wait_time / 100} ---".center(89))
    time.sleep(random_wait_time / 100)

    result = requests.get(url, timeout=10)
    connections_made += 1
    print(f"--- Current connnection request: {connections_made} ---".center(89))

    ## 200 means not banned
    if result.status_code != 200:
        print(f"--- ErrorCode {result.status_code} ---".center(89))
        break
    print(f"--- Code {result.status_code}: Connection Valid ---\n".center(89))

    soup = BeautifulSoup(result.content, "lxml")
    tags = soup.findAll("div", {"class": "item-container"})
    cards = []
    stock = []
    prices = []

    if instock_found > 0:
        if send_email_confirmation is True:
            send_email(bot_email, bot_key, mail_to)
            print(f"--- Email sent, automatic messages turned off. ---".center(89))
            send_email_confirmation = False

        print("\n", f"--- {instock_found} item(s) reported IN STOCK ---\n\n".center(89))

    ## Checks for in/out of stock
    for i in range(len(tags)):

        # Grabs the titles of all products
        if tags[i].find("a", {"title": "View Details"}) is None:
            cards.append("promotional item")
        else:
            cards.append(str(tags[i].find("img").attrs["title"][:60]))

        # Checks availability
        if tags[i].find("div", {"class": "item-info"}).p is None:
            stock.append("---IN STOCK---")
            instock_found += 1

        else:
            if str(tags[i].find("div", {"class": "item-info"}).p.get_text()) == "OUT OF STOCK":
                stock.append("-OUT OF STOCK-")
            else:
                stock.append("---IN STOCK---")
                instock_found += 1

        # Grabs the prices of all products
        if tags[i].find("div", {"class": "item-action"}) is None:
            prices.append("0")
        else:
            if tags[i].find("div", {"class": "item-action"}).strong is None:
                prices.append("0")
            else:
                prices.append(str(tags[i].find("div", {"class": "item-action"}).strong.get_text()))

    ## Formatting for display
    prices = [int(i.replace(",", "")) for i in prices]
    lines = [(z, y, x) for x, y, z in zip(cards, stock, prices) if x != "promotional item"]

    for a, b, c in sorted(lines, reverse=True):
        a = "{:,}".format(a)

        print(f"{('$' + a).rjust(6)} - {b.center(14)} - {c.ljust(28)+'...'}")
