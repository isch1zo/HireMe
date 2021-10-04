import time
import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import mimetypes


def send_mail(mail, CV, letter):
  # mail text content
  if check == 'y':
    mail_content = ('''
Dear HR Team, 
I am writing this email to express my interest in having my summer training in your company.
I am Senior Computer Science student from '''+SchoolName+''' with a major GPA: '''+GPA+''' .interested in the '''+field+''' field. I have professional certifications in the field such as: '''+certs+''', and others.
I am confident that my skills would be put to good use at your company, and I would enjoy the opportunity to work with you and collaborate with your team.
For more information, you will find my CV and eligibility letter in the attachments.
Thanks for considering my application, I look forward to hearing from you.
Best Regards,
'''+Name+'''
'''+pos+''',
'''+SchoolName+'''
phone number: '''+Phone+'''
    ''')
  else:
    mail_content = New_content
  # The mail addresses and password
  sender_address = email
  sender_pass = passwd

  # reciever mail will be gotten from the file and passed as function argument
  receiver_address = mail

  # Setup the MIME
  message = MIMEMultipart()
  message['From'] = sender_address
  message['To'] = receiver_address
  message['Subject'] = subject  # The subject line CHANGE THIS IF YOU NEED

  # The body and the attachments for the mail
  message.attach(MIMEText(mail_content, 'plain'))

  # ATTACH THE CV FILE
  # attach_file_name = 'CV.pdf'
  attach_file_name = CV
  with open(attach_file_name, "rb") as fil:
    content_type = mimetypes.guess_type(attach_file_name)[0].split("/")
    part = MIMEBase(content_type[0], content_type[1])
    part.set_payload(fil.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % basename(attach_file_name))
    message.attach(part)

  # ATTACH THE LETTER FILE
  # attach_file2_name = 'letter.pdf'
  attach_file2_name = letter
  with open(attach_file2_name, "rb") as fil2:
    content_type = mimetypes.guess_type(attach_file2_name)[0].split("/")
    part2 = MIMEBase(content_type[0], content_type[1])
    part2.set_payload(fil2.read())
    encoders.encode_base64(part2)
    part2.add_header('Content-Disposition', "attachment; filename= %s" % basename(attach_file2_name))
    message.attach(part2)

  # Create SMTP session for sending the mail
  session = smtplib.SMTP('smtp.gmail.com', 587)
  session.starttls()  # enable tls security
  session.login(sender_address, sender_pass)  # login with mail and password
  text = message.as_string()
  session.sendmail(sender_address, receiver_address, text)
  session.quit()
  print("Mail Sent")


if __name__ == "__main__":


  email = input("Enter email: ")
  passwd = input("password: ")



  # Enter the mail list file
  # mails = "mails.txt"
  subject = input("Enter the email subject. Ex :{Summer Training} :")
  mails = input("Enter mails file: ")
  CV = input("Enter CV file path: ")
  letter = input("Enter Letter file path: ")

  print(" ")
  print("********************************************************************************************************************************************************************"
        "\n**                                                                                                                                                              **"
        "\n** Dear HR Team, I am writing this email to express my interest in having my summer training in your company.                                                   **"
        "\n** I am Senior Computer Science student from [Your University name] with a major GPA: [Your major GPA]. interested in                                            **"
        "\n** the [Your interest field] field. I have professional certifications in the field such as:[List Your certs here], and others.                                 **"
        "\n** I am confident that my skills would be put to good use at your company, and I would enjoy the opportunity to work with you and collaborate with your team.   **"
        "\n** For more information, you will find my CV and eligibility letter in the attachments.                                                                         **"
        "\n** Thanks for considering my application, I look forward to hearing from you.                                                                                   **"
        "\n** Best Regards,                                                                                                                                                **"
        "\n** [Your name]                                                                                                                                                  **"
        "\n** Senior Computer Science Student,                                                                                                                             **"
        "\n** [Your University name]                                                                                                                                       **"
        "\n** phone number: [Your phone number]                                                                                                                            **"
        "\n**                                                                                                                                                              **"
        "\n********************************************************************************************************************************************************************")
  print(" ")
  check = input("Do you want to use the above as your E-mail content? (y/n)")
  print(" ")

  if check == 'y':
      Name = input("Your Name: ")
      Phone = input("Phone number : ")
      SchoolName = input("University name : ")
      GPA = input("GPA: ")
      field = input("field of interest, Ex : {CyberSecurity}:")
      certs = input("Enter Certificates you've achieved (Separated by comma): ")
      pos = input("Enter your position , Ex :{Senior Computer Science Student}")
  else:
      f=open(input("Enter your E-mail content path :"),"r")
      New_content = (f.read())




  mails_file = open(mails, "r")
  for mail in mails_file:
    print("[+] Sending Email to: " + mail)
    send_mail(mail, CV, letter)
    time.sleep(3)
