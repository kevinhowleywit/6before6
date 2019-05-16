import requests
from bs4 import BeautifulSoup
import config
import smtplib
def main():

    createMessage()


def sendMail(msg,subject):
    #print("Today's 6 before 6 is " + h_data)
    emails=getContacts('contacts.txt')

    for x in range(len(emails)):
        print(emails[x])
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(config.EMAIL_ADDRESS, config.PASSWORD)
            message = 'Subject: {}\n\n{}'.format(subject, msg)
            server.sendmail(config.EMAIL_ADDRESS, emails[x], message)
            server.quit()
            print("Success: Email sent!")
        except:
            print("Email failed to send.")


def getContacts(filename):
    #print('got this far')
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            emails.append(a_contact.split()[0])

    return emails



def createMessage():
    ramen_url = 'https://ramen.ie/whats-the-6before6/'
    ramen_response = requests.get(ramen_url, timeout=5)
    soup = BeautifulSoup(ramen_response.content, "html.parser")
    # print(soup.prettify())
    h_data = soup.find_all('h2')[0].get_text()

    #print("Today's 6 before 6 is "+h_data)
    subject = "Today's 6 before 6"
    msg = "Hello \nThis is an automated email.\nToday's 6 before 6 is "+ h_data
    sendMail(msg,subject)
    #print(subject)
    #print(msg)


# main route
main()
