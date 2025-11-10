# create class for sending messages via WhatsApp

import pywhatkit
from datetime import datetime

class SendMessage:

    # initiate class
    # phoneNumber must be a string
    def __init__(self, phoneNumber, message):
        self.phoneNumber = phoneNumber
        self.message = message
        self.hour = datetime.now().hour
        self.minute = datetime.now().minute + 2
        self.delay = 60

    # prints all properties of class object
    def __str__(self):
        return f"Phone Number: {self.phoneNumber}\nMessage: {self.message}\nHour: {self.hour}\nMinute: {self.minute}\nDelay: {self.delay}"

    # sends message with pywhatkit
    def sendMessage(self):
        pywhatkit.sendwhatmsg(self.phoneNumber, self.message, self.hour, self.minute, self.delay)