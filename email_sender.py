# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

 # Create a text/plain message
email = EmailMessage()
email.set_content('Testing on emails sending')

# me == the sender's email address
# you == the recipient's email address
email['Subject'] = 'Testing on emails sending via Python'
email['From'] = "Jason Tam"
email['To'] = 'jasonyst93@gmail.com'


with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo() #sending hello
    smtp.starttls() #encripy 
    smtp.login('jasonyst93test@gmail.com','oxah apbd cjlm exph') #login with app password (youtube)
    smtp.send_message(email) #sending an email

