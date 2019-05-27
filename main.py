import requests
from bs4 import BeautifulSoup
from datetime import date
import config
import smtplib
def main():

    createMessage()


def sendMail(msg,subject):

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

    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            emails.append(a_contact.split()[0])

    return emails



def createMessage():

    ramen_url = 'https://ramen.ie/whats-the-6before6/'
    ramen_response = requests.get(ramen_url, timeout=5)
    soup = BeautifulSoup(ramen_response.content, "html.parser")
    h_data = soup.find_all('h2')[0].get_text()

    #send h_data to a text file
    write_to_file(h_data)

    #start putting the message together
    subject = "Today's 6 before 6"
    msg = "Hello \nThis is an automated email.\nToday's 6 before 6 is "+ h_data+"\nBest regards\nMDR guy."
    sendMail(msg,subject)

#function to record history of previous 6 before 6s

def write_to_file(h_data):
    print(h_data)
    today = str(date.today())
    string_to_write = h_data + "-" + today
    history_file=open("historyFile.txt", "a")
    history_file.write(string_to_write+"\n")
    history_file.close()

    # main route
main()
