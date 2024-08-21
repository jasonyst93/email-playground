import smtplib
from email.message import EmailMessage

#Two more built-in libraries!!
#Subsitle variable into text
from string import Template

#Read/Access the HTML file
from pathlib import Path #smiliar to os.path

#Access(Path) and read the text(.read_text()) from index.html and transfer to a Template object(Template) 
html = Template(Path('index.html').read_text())

 # set content to a Templated object (html) with substitue
email = EmailMessage()
email.set_content(html.substitute({'name': 'Hanni'}),'html') # substitute name = Hanni and tell it's html

email['Subject'] = 'Testing on emails sending via Python'
email['From'] = "Jason Tam"
email['To'] = 'jasonyst93@gmail.com'


with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo() 
    smtp.starttls() 
    smtp.login('jasonyst93test@gmail.com','oxah apbd cjlm exph') 
    smtp.send_message(email)

