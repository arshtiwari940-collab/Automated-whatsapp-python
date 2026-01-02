from twilio.rest import Client
from datetime import datetime, timedelta
import time
account_sid = 'YOUR ACCOUNT SID'
auth_token = 'YOUR AUTH TOKEN NUMBER'
client = Client(account_sid, auth_token)
def send_watsmsg(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f"Message sent successfully msg SID {message.sid}")
    except Exception as e:
        print("An error occurred")
        print(e)
name = input("Enter the recipient name: ")
recipient_number = input(f"Enter the recipient number with country code")
message_body = input(f"Enter the message to send to {name}: ")
date_str = input("Enter the date to send the message (YYYY-MM-DD) format: ")
time_str = input("Enter the time to send the message (HH:MM) 24hr format: ")
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()
if delay_seconds <= 0:
    print("This message could not be sent. The specified time is in the past.")
else:
    print(f"Message scheduled to be sent to {name} at {schedule_datetime}")
    time.sleep(delay_seconds)
    send_watsmsg(recipient_number,message_body)
