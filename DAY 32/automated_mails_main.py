import smtplib
import datetime
import random
import pandas

month = datetime.date.today().month
day = datetime.date.today().day
my_email = "abdalrahmank2000@gmail.com"
my_password = "yupy jbsh lmok tpko"

today = (month, day)

data = pandas.read_csv("birthdays.csv")

new_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in new_dict:
    person = new_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as file:
        file_content = file.read()
        file_content = file_content.replace("[NAME]", person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email, to_addrs=person["email"],
                            msg=f"Subject: Happy Birthday\n\n{file_content}")
