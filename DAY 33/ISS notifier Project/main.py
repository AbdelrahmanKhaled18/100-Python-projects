import requests
from datetime import datetime
import smtplib
import time
import config


def is_iss_overhead():
    response = requests.get(url="https://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return (config.MY_LAT - 5 <= iss_latitude <= config.MY_LAT + 5 and
            config.MY_LONG - 5 <= iss_longitude <= config.MY_LONG + 5)


def is_night():
    parameters = {
        "lat": config.MY_LAT,
        "lng": config.MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.utcnow().hour
    return time_now >= sunset or time_now <= sunrise


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(config.MY_EMAIL, config.MY_PASSWORD)
            connection.sendmail(
                from_addr=config.MY_EMAIL,
                to_addrs=config.MY_EMAIL,
                msg="Subject:Look Up 👆\n\nThe ISS is above you in the sky!"
            )
