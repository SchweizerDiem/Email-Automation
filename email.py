import smtplib


# using and accessing smtplib server.
def send_email():
    email_from = input("Enter email account: ")
    email_to = input("Enter email message is been sent to: ")
    email_password = input("Enter you APP password: ")
    subject = input("Type the subject of the email: ")

    find_index_AT = email_from.find("@")
    email_service = email_from[find_index_AT + 1 :]

    if email_service == "gmail.com":
        enter_service_on_smtp = "smtp.gmail.com"
    elif email_service == "outlook.com":
        enter_service_on_smtp = "smtp.outlook.com"
    elif email_service == "hotmail.com":
        enter_service_on_smtp = "smtp.hotmail.com"
    else:
        print(
            f"{email_service} is not an acceptable email service. Please enter another one."
        )

    conn = smtplib.SMTP(f"enter_service_on_smtp", 587)
    # Start connection with stmp server
    conn.ehlo()
    # Encript message
    conn.starttls()

    conn.login(f"{email_from}", f"{email_password}")

    conn.sendmail(f"{email_from}", f"{email_to}", f"Subject: {subject}")

    conn.quit()


# executing main program.
def main():
    entry = print("Are you sure you wanna send an email?(y/n) ")

    if entry == "y".lower():
        send_email()

    print("Bye.")


if __name__ == "__main__":
    main()
