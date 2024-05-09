import smtplib

my_mail = "vinay588325@gmail.com"
passwd = "unujdqdqbskvhmwk"

connection = smtplib.SMTP(host="142.251.175.109")
connection.starttls()
connection.ehlo()
connection.login(user=my_mail, password=passwd)
connection.sendmail(to_addrs=["mail2vnyd@gmail.com", "vinaymatam@kpmg.com"], msg="Hello")
connection.close()

# import datetime as dt

# print(dt.datetime.now())