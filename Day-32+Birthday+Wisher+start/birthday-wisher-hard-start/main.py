import pandas
from datetime import date
import random
import smtplib
##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 
df = pandas.read_csv("./birthday-wisher-hard-start/birthdays.csv")
len_doc = len(df)
# print(len(df))
# print(df.iloc[1]["month"])
# print(df.iloc[1]["day"])
birthdays_dict = {(df.iloc[i]["month"], df.iloc[i]["day"]):i for i in range(0,len_doc)}
# print(birthdays_dict)
# rand_letter = random.randint(1,3)
# file = "./birthday-wisher-hard-start/letter_templates/letter_" + str(rand_letter) +".txt"
# print(file)
# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
def send_email(to_addr, body):
    my_mail = "vinay588325@gmail.com"
    passwd = "unujdqdqbskvhmwk"
    connection = smtplib.SMTP(host="142.251.175.109")
    connection.starttls()
    connection.ehlo()
    connection.login(user=my_mail, password=passwd)
    connection.sendmail(to_addrs=to_addr, msg=f"Subject:HappyBirthday\n\n{body}")
    connection.close()




today = date.today()
if (today.month, today.day) in birthdays_dict:
    index = birthdays_dict.get((today.month, today.day))
    rand_letter = random.randint(1,3)
    file = "./birthday-wisher-hard-start/letter_templates/letter_" + str(rand_letter) +".txt"
    with open(file) as letter:
        content = letter.read()
        content = content.replace("[NAME]", df.iloc[index]["name"])
        send_email(df.iloc[index]["email"], content)
# # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

# print(f"{today.month} {today.day}")
# print(birthdays_dict.get((today.month, today.day)))

