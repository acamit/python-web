import datetime as dt
import random
import smtplib

MY_EMAIL = "acamit84@gmail.com"
MY_PASSWORD = "fclskebcykqhuuce"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open('quotes.txt') as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation \n\n {quote}")



#
# # get quote from api
# response = requests.get("https://api.kanye.rest/")
# print(response.json())
#
# quote = response.json()["quote"]
# print(quote)


