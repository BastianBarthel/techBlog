import os
import smtplib

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
SMTP = "smtp.gmail.com"


class Mail:

    def send_mail(self, name, email, phone, message):
        with smtplib.SMTP(SMTP) as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f"Subject:New Contact\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}".encode("utf-8")
            )
