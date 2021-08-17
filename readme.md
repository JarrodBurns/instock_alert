# Newegg In stock Alert
This alerter is configured to monitor a **valid url**. Upon identifying an in stock item it sends an **email** to the user about what was found.

![smaple_log](https://user-images.githubusercontent.com/87616660/129764445-b37f8936-f0cf-4a62-a54a-d08fc59b2bb6.png)

## What is a valid URL?
A valid URL is a newegg search page or event sale store page. This program **does not** accept individual item pages. If you are looking for something specific try to narrow your search terms.

## What Email?
If you wish to receive an email when you find a result, you will need to set up a gmail account with the option **allow less secure apps** set to **ON**.

Once you have your email and password, open the file **hidden.py** and input your credentials.

    bot_email = "your_bot_gmail@gmail.com"
    bot_key = "your_bot_password"  
    mail_to = "your_real_email@email.com"

Currently the bot is configured to turn email sending off after an alert.

This means if you set send_alert to True and find an in stock item you will need to restart the program before it will send an alert again. I prefer it this way, but sleep would also work well here if you wanted to change it.

## Version Control
Newegg In stock Alert is dependent on the following:

- [python](https://docs.python.org/3/) 3.9.6
- [yagmail](https://yagmail.readthedocs.io/en/latest/setup.html) 0.14.256
- [requests](https://docs.python-requests.org/en/master/) 2.26.0
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) 4.9.3

## Conclusion
Thank you for taking the time to review the readme, if you have any questions feel free to message my twitter bot, @BotJarrod or my gmail at ta747839@gmail.com


