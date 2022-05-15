import re
import smtplib


class sender:
    def __init__(self):
        self.smtpObj = None
        self.senderid = None
        self.password = None

    def get_connection(self, senderid, password):
        try:
            self.smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            self.smtpObj.starttls()
            self.smtpObj.login(senderid, password)
            print("Successfully logged in")
        except Exception:
            print("Error !! unable to login")

            self.smtpObj.quit()

    def send_mail(self, reciver, subject, body, sendername=None):
        if sendername==None:
            sendername=self.senderid
        sub = "Subject:" + subject + "\n"
        message = sub + body
        message=message.encode('utf-8').strip()

        try:
            self.smtpObj.sendmail(sendername, reciver, message)
            print("sucessfully mail sent")
            self.smtpObj.quit()
        except Exception as e:
            print(e)
            print("Error !!  unable to send mail")
            self.smtpObj.quit()
