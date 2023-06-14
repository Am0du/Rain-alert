import requests
import smtplib
import json
import os

with open('contact.json') as file:
    data1 = json.load(file)

contact_data = data1['users']

for contact in contact_data:
    my_email = 'damodu647@gmail.com'
    password = os.environ.get('email_pass')
    parameter = {
        'q': f"{contact['location']}",
        'appid': os.environ.get("API_key"),
        'units': 'metric'
    }


    response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast', params=parameter)
    response.raise_for_status()
    data = response.json()

    rain = None
    for _ in range(7):
        weather_id = int(data['list'][_]['weather'][0]['id'])
        if weather_id < 700:
            rain = True
            break
        else:
            rain = False

    if rain:
        msg = 'if them born you well, commot house without umbrella!!!'
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=f"{contact['email']}",
                                msg=f"Subject:Amodu, your neighbourhood weather man\n\nSAYS:\n\nDear {contact['name']},"
                                    f"\n\n{msg}")

    else:
        msg = 'Today is a good day to glow, glow baby glow!!!'
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=f"{contact['email']}",
                                msg=f"Subject:Amodu, your neighbourhood weather man\n\nSAYS:\n\nDear {contact['name']},"
                                    f"\n\n{msg}")
