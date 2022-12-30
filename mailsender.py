import time, smtplib, mimetypes, ssl
from os.path import basename
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import EmailMessage


def send_mail(login, password, subject, cv_path, receiver_address):

    # Mail Content FIX THIS
    mail_content = """
    Hello HR Team,

    I wish to apply for the position of [Name of the Position] that is listed on your website. The role and the responsibilities listed in the job description match my interests and skills. I believe that I’m a good candidate for this position.

    I have attached my resume. I hope they can help you learn more about my background, my qualifications, and my experience.

    Thank you for your valuable time. I’m optimistic that you’ll consider me for this role. I look forward to hearing from you about this job opportunity.
    
    Sincerely,
    [Your Name]
    [Contact Number]
    [Email]
    """

    # The mail addresses and password
    sender_address = login
    sender_pass = password

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject

    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    
    # Attach the CV file 
    with open(cv_path, "rb") as fil:
        content_type = mimetypes.guess_type(cv_path)[0].split("/")
        part = MIMEBase(content_type[0], content_type[1])
        part.set_payload(fil.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % basename(cv_path))
        message.attach(part)


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_address, sender_pass)
        server.send_message(message, from_addr=sender_address, to_addrs=receiver_address)
        print(f"[+] Email sent to: {receiver_address}")

if __name__ == "__main__":
    login = input("Enter Your Email: ")
    password = input("Enter App Key password: ")
    subject = input("Enter subject: ")
    cv_path = input("Enter CV path: ")
    mails = input("Enter Mails list file path: ")
    mails_file = open(mails, "r")
    for mail in mails_file:
        send_mail(login, password, subject, cv_path, mail)
        time.sleep(3)
