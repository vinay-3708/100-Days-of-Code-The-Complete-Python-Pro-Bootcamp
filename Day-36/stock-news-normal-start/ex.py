# import json
# from datetime import date
# from datetime import timedelta
# data = {
#     "Meta Data": {
#         "1. Information": "Daily Prices (open, high, low, close) and Volumes",
#         "2. Symbol": "IBM",
#         "3. Last Refreshed": "2024-05-21",
#         "4. Output Size": "Compact",
#         "5. Time Zone": "US/Eastern"
#     },
#     "Time Series (Daily)": {
#         "2024-05-21": {
#             "1. open": "169.9400",
#             "2. high": "174.9700",
#             "3. low": "169.9400",
#             "4. close": "173.4700",
#             "5. volume": "6459800"
#         },
#         "2024-05-20": {
#             "1. open": "169.0000",
#             "2. high": "170.1600",
#             "3. low": "168.3800",
#             "4. close": "169.9200",
#             "5. volume": "2726261"
#         }
#     }
# }
# print(data['Time Series (Daily)'])
# today = date.today()
# print('Today :' + str(today))
# print('Yesterday :' + str(today - timedelta(days=1)))
# print('DayBY :' + str(today - timedelta(days=2)))
# print(data['Time Series (Daily)'][str(today - timedelta(days=1))]["4. close"])



# from twilio.rest import Client

# account_sid = 'XXXXXXXXXXX'
# auth_token = 'XXXXXXXXXXXXXXXXXX'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#   from_='whatsapp:+14155238886',
#   body='Your Twilio code is 1238432',
#   to='whatsapp:+917660999887'
# )

# print(message.sid)
# print(message.status)
# print(message.body)

from twilio.rest import Client

account_sid = 'XXXXXXXXXXXXXXXXXXX'
auth_token = 'XXXXXXXXXXXXXXXXXXXXXXXX'
client = Client(account_sid, auth_token)

from_num='+15515507509'

message = client.messages.create(
  from_=from_num,
  body='Test Msg from Twilio using Variables',
  to='+917660999887'
)


print(message.sid)
print(message.status)